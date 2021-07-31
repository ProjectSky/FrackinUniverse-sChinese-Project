-- 判断utf8字符byte长度
-- 0xxxxxxx - 1 byte
-- 110yxxxx - 192, 2 byte
-- 1110yyyy - 225, 3 byte
-- 11110zzz - 240, 4 byte
local function chsize(char)
	if not char then
		print("not char")
		return 0
	elseif char > 240 then
		return 4
	elseif char > 225 then
		return 3
	elseif char > 192 then
		return 2
	else
		return 1
	end
end

-- 计算utf8字符串字符数, 各种字符都按一个字符计算
-- 例如utf8len("1你好") => 3
function utf8len(str)
	local len = 0
	local currentIndex = 1
	while currentIndex <= #str do
		local char = string.byte(str, currentIndex)
		currentIndex = currentIndex + chsize(char)
		len = len + 1
	end
	return len
end

-- 截取utf8 字符串
-- str:			要截取的字符串
-- startChar:	开始字符下标,从1开始
-- numChars:	要截取的字符长度
function utf8sub(str, startChar, numChars)
	local startIndex = 1
	while startChar > 1 do
		local char = string.byte(str, startIndex)
		startIndex = startIndex + chsize(char)
		startChar = startChar - 1
	end

	local currentIndex = startIndex

	while numChars > 0 and currentIndex <= #str do
		local char = string.byte(str, currentIndex)
		currentIndex = currentIndex + chsize(char)
		numChars = numChars - 1
	end
	return str:sub(startIndex, currentIndex - 1)
end

-- 搜索指定字符串在utf8字符串的位置
-- str:			utf8字符串
-- pattern:		搜索字符串
-- init:		初始索引
function utf8find(str, pattern, init)
	local b,e = string.find(str, pattern, init)
	if b == nil then return nil end
	local count = 1
	local beginPos = 0
	local endPos = 0
	local currentIndex = 1
	while currentIndex <= #str do
		if b == currentIndex then
			beginPos = count
		end
		if e < currentIndex then
			endPos = count - 1
			return beginPos, endPos
		end
		if e == currentIndex then
			endPos = count
			return beginPos, endPos
		end
		local char = string.byte(str, currentIndex)
		currentIndex = currentIndex + chsize(char)
		count = count + 1
	end
	if e == #str then
		endPos = count
		return beginPos, endPos
	end
	return nil, nil
end