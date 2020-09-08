	Created By 微风的龙骑士 风游迩 
	部分特殊名词的参考文档
  
	第一个中文名为目前统一使用的译名，后面的为可考虑的或者曾用的。  
	请其他项目参与者协助扩充。  
	全局搜索`@?`：极其不确定的翻译。

# TODO

- [ ] 验证护甲的效果
- [ ] 验证护甲、武器的升级关系（在工具升级台中，而非提升武器等级后，自动升级）

* 验证：
	* 人物创建界面：Brand，CH4，HUMAN，Ne，UNDY COLOR，Warrior race from the Kortakk nebula等

&emsp;

# 模版

## 通用

```
青色：通用正面效果。
紫色：武器的条件效果。
亮红色：生态的条件效果。
绿色：附加效果，描述性的效果。
黄色：特性。
红色：通用负面效果。

橙色：突出显示的数值或范围。

橙色：任务接收
绿色：任务回报

蓝色：译注

表示可升级工具/武器/护甲的等级：在名称后面加上“ [LX]”，其中X表示等级。

通用效果的排列顺序：能力值调整；抗性调整；状态抵抗和免疫；附加效果（如：发光，赋予状态）
```

## 武器

### 格式规范

```
（描述文字）
（效果，归类）
（特性，次要攻击说明）
（负面效果）
```

## 盾牌

### 格式规范

```
（可能的描述文字）
（正面效果）
（附加效果，描述性的效果）
（负面效果）
```

## 护甲

### 格式规范

```
套装效果：
（通用正面效果）
（武器的条件效果）
（生态的条件效果）
（附加效果，描述性的效果）
```

## 状态（来自套装效果）

### 格式规范

```
（无条件效果）
（武器类别，“&”表示双持不同种类的武器）：（有条件效果）
（生态类别）：（有条件效果）
```

### 示例

&emsp;

# 参考

## 玩家属性

### 标准属性（三度仪中注明的高级属性）

* 生命值上限&emsp;Max Health&emsp;Health&emsp;［默认：100］
* 生命回复速度&emsp;Health Regen %&emsp;Regen %&emsp;［默认：0］
* 防御力&emsp;Protection&emsp;Defense, DEF&emsp;［默认：0］
&emsp;
* 能量值上限&emsp;Max Energy&emsp;Energy&emsp;［默认：100］
* 能量回复速度&emsp;Energy Regen %
* 能量回复时间&emsp;Energy Regen Time
&emsp;
* 攻击力倍率&emsp;Power Multiplier %&emsp;Attack, Power, Rage?&emsp;［默认：100%］
* 暴击伤害加成&emsp;Grit Damage Bonus +%&emsp;Crit Damage, Crit Dmg
* 暴击几率&emsp;Grit Chance +%&emsp;Crit %, Crit Chance %, Critical Chance %
&emsp;
* 呼吸时限&emsp;Breath Duration&emsp;Oxygen %, Oxygen Supply %
* 呼吸回复速度&emsp;Breath Regen
* 饥饿速度&emsp;Food Consumption per second&emsp;Hunger, Hunger Rate
&emsp;
* 击退抵抗&emsp;Knockback Resistance %
* ？？？临界值&emsp;？？？ Threshold
* 掉落伤害&emsp;Fall Damage %
&emsp;
* 盾牌反伤几率&emsp;Shield Bash Chance, Shield Bash?
* 盾牌击退&emsp;Shield Bash Push, Shield Push?
* 飞船质量&emsp;Ship Mass

### 所有属性

* 生命值上限&emsp;Max Health&emsp;Health&emsp;［默认：100］
* 生命回复速度&emsp;Health Regen %&emsp;Regen %&emsp;［默认：0］
&emsp;
* 能量值上限&emsp;Max Energy&emsp;Energy&emsp;［默认：100］
* 能量回复速度&emsp;Energy Regen %
* 能量回复时间&emsp;Energy Regen Time
&emsp;
* 攻击力，攻击力倍率&emsp;Power Multiplier %&emsp;Attack, Power, Rage?&emsp;［默认：100%］
* 防御力&emsp;Protection&emsp;Defense, DEF&emsp;［默认：0］
&emsp;
* 暴击伤害，暴击伤害加成&emsp;Grit Damage Bonus +%&emsp;Crit Damage, Crit Dmg
* 暴击几率&emsp;Grit Chance +%&emsp;Crit %, Crit Chance %, Critical Chance %
&emsp;
* 伤害&emsp;Dmg,Damage
* 护甲&emsp;Armor
&emsp;
* 呼吸时限&emsp;Breath Duration&emsp;Oxygen %
* 呼吸回复速度&emsp;Breath Regen
* 饥饿速度&emsp;Food Consumption per second&emsp;Hunger
&emsp;
* 击退抗性&emsp;Knockback Resistance %, Knockback Resist
* ？？？临界值&emsp;？？？ Threshold
&emsp;
* 掉落速度&emsp;Fall Speed
* 掉落伤害&emsp;Fall Damage %
&emsp;
* 跳跃力&emsp;Jump
* ？？？&emsp;Air Force
* 移动速度&emsp;Speed
* 游泳速度&emsp;Swim
&emsp;
* 盾牌反伤&emsp;Shield Bash Chance, Shield Bash?
* 盾牌击退，盾牌反伤击退&emsp;Shield Bash Push, Shield Push?, Knockback?
* 盾牌耐久&emsp;Shield Health, Stamina
* 盾牌耐久回复速度&emsp;Shield Regen
* 格挡几率？&emsp;Block, Blocking
* 完美格挡时间&emsp;Perfect Block Time
&emsp;
* 飞船质量&emsp;Ship Mass
* 飞船行驶速度&emsp;ship speed
* 飞船燃料利用率&emsp;fuel efficiency
* 飞船燃料容量&emsp;maximum fuel capacity

## 玩家属性（未整理）

### 一般

* 生命值上限&emsp;Health,Max Health
* 能量值上限,&emsp;Energy,Max,Energy
* 生命回复速度&emsp;Health Regen
* 能量回复速度&emsp;Energy Regen
* 黑暗回复速度&emsp;Darkness Regen
* 呼吸时限&emsp;% Oxygen
* 掉落速度&emsp;Fall Speed
* 饥饿速度&emsp;Hunger
* 跳跃力&emsp;Jump
* 移动速度&emsp;Speed
* 游泳速度&emsp;Swim
* 掉落伤害&emsp;Fall Damage

### 攻击相关

* 攻击&emsp;Attack,Power(?),Rage(?)
* 伤害&emsp;Dmg,Damage
* 防御&emsp;DEF,Protection
* 护甲&emsp;Armor
* 暴击几率&emsp;Crit,Crit Chance,Critical Chance
* 暴击伤害&emsp;Crit Damage
* 眩晕几率&emsp;Stun Chance

### 盾牌相关

* 盾牌耐久&emsp;Shield Health,Stamina
* 盾牌耐久回复速度&emsp;Shield Regen
* 盾牌反伤&emsp;Shield Bash
* 盾牌击退&emsp;Shield Push,Knockback
* 盾牌精通&emsp;Shield Mastery
* 盾牌格挡几率？&emsp;Block？
* 完美格挡时间&emsp;Perfect Block Time

### 飞船相关

* 飞船行驶速度&emsp;ship speed
* 飞船燃料利用率&emsp;fuel efficiency
* 飞船燃料容量&emsp;maximum fuel capacity
* 飞船质量&emsp;Ship Mass

## 元素属性

* 物理属性&emsp;Physical
* 射线属性&emsp;Cosmic
* 寒气属性&emsp;Ice
* 火炎属性&emsp;Fire
* 电系属性&emsp;Electric
* 毒素属性&emsp;Poison
* 射线属性&emsp;Radiation
* 暗影属性&emsp;Shadow

## 分类法

### 武器分类

**单手近战武器**

* 匕首&emsp;Dagger
* 短剑&emsp;Short Sword
* 长剑&emsp;Long Sword
* 刺剑，细剑&emsp;Rapier
* 短矛，短枪&emsp;Short Spear
* 斧&emsp;Axe
* 钉头锤，锤矛&emsp;Mace
* 武士刀&emsp;Katana
* 战剑&emsp;War Sword
* 战刃&emsp;Warblade

**双手武器**

* 宽剑&emsp;Cleaver
* 矛，长矛，枪&emsp;Spear
* 长矛，长枪&emsp;Lance, fu_lance
* 巨斧，大斧&emsp;Great Axe
* 锤，槌&emsp;Hammer
* 长棍&emsp;Quarterstaff
* 镰刀&emsp;Scythe
* 武士刀&emsp;Katana
 
**射击武器（不包括枪械）**

* 弓&emsp;Bow
* 弩&emsp;Crossbow

**护身/投掷武器**

* 拳套&emsp;Fists
* 鞭&emsp;Whip
* 环刃&emsp;Chakram
* 回旋镖&emsp;Boomerang
* 磁力珠&emsp;Magnorb
* 打击者&emsp;Striker

**手枪**

* 手枪&emsp;Pistol
* 自动手枪&emsp;Machine Pistol
* 左轮手枪&emsp;Revolver
* 霰弹手枪&emsp;Shotgun Pistol

**轻枪械**

* 步枪&emsp;Rifle
* 突击步枪&emsp;Assault Rifle
* 霰弹枪&emsp;Shotgun
* 狙击步枪&emsp;Sniper Rifle
* 冲锋枪&emsp;Submachine Gun
* 战斗步枪&emsp;Battle Rifle
* 反器材步枪&emsp;AntiMaterial Rifle
* 卡宾枪&emsp;Carbine

**重枪械**

* 火箭发射器&emsp;Rocket Launcher
* 榴弹发射器&emsp;Grenade Launcher
* 利刃发射器&emsp;Claw Launcher
* 加农炮&emsp;Cannon
* 轨道炮&emsp;Rail Gun
* 高射炮&emsp;Flak Cannon

**其他**

* 物质枪&emsp;Matter Manipulator

**魔法触媒**

* 魔杖（单手）&emsp;Staff
* 法杖（双手）&emsp;Wand

### 武器系列

* 剑刃武器&emsp;Bladed Weapons
* 近战武器&emsp;Melee Weapons
* 狩猎武器&emsp;Hunting Weapons
* 自动武器&emsp;Squad Automatic Weapons
&emsp;
* 能量武器&emsp;Energy Weapons
* 等离子武器，电浆武器&emsp;Plasma Weapons
* 动能武器，动力武器&emsp;Kinetic Weapons
* 液体武器&emsp;Liquid Weapons
* 激光武器&emsp;Beam Weapons
* 重力武器&emsp;Gravity Weapons
&emsp;
* 生物武器&emsp;Bio-Weapons
* 黏液武器&emsp;Slime Weapons
* 真菌武器&emsp;Spawn Weapons
&emsp;
* 月晶武器&emsp;Lunari Weapons
* 棱镜武器&emsp;Prismatic Weapons
* 寂灭武器&emsp;Quietus Weapons
* 先驱武器&emsp;Precursor Weapons
* 赛德瑞瑟武器&emsp;Xithricite Weapons
&emsp;
* 电系武器&emsp;Electric Weapons
* 火炎武器&emsp;Fire Weapons
* 寒气武器&emsp;Ice Weapons
* 放射武器&emsp;Radiation Weapon

## 物品

### 矿石 & 锭

**原版**

* 铜矿石&emsp;Copper Ore
	［生成］铜锭&emsp;Copper Bar
* 铁矿石&emsp;Iron Ore
	［生成］铁锭&emsp;Iron Bar
* 银矿石&emsp;Silver Ore
	［生成］银锭&emsp;Silver Bar
* 金矿石&emsp;Gold Ore
	［生成］金锭&emsp;Gold Bar
* 钨矿石&emsp;Tungsten Ore
	［生成］钨锭&emsp;Tungsten Bar
* 钛矿石&emsp;Titanium Ore
	［生成］钛锭&emsp;Titanium Bar
* 耐钢矿&emsp;Durasteel Ore
	［生成］耐钢锭&emsp;DuraSteel Bar
* 霓磷盐矿&emsp;Aegisalt Ore
	［生成］精炼霓磷盐&emsp;Refined Aegisalt
* 维奥合金矿&emsp;Violium Ore 
	［生成］精炼维奥合金&emsp;Refined Violium
* 菲洛合金矿&emsp;Ferozium Ore 
	［生成］精炼菲洛合金&emsp;Refined Ferozium
* 日耀石矿&emsp;Solarium Ore
	［生成］精炼日耀石&emsp;Refined Solarium
&emsp;
* 星核碎片&emsp;Core Fragment Ore
* 水晶&emsp;Crystal
* 钻石&emsp;Diamond
* 冰晶体&emsp;Ice crystal
* 硫磺&emsp;Sulphur
&emsp;
* 原力石矿？？？ -> 原力矿
* 棱镜碎片？？？
* 精简的棱镜碎片 -> 棱镜之星
* 月石矿 -> 特勒贝晶体

**FU**

* 碳&emsp;Carbon
	［生成］碳板&emsp;Carbon Plate
* 黑檀石碎片&emsp;Ebon Shard
* 琥珀块&emsp;Amber Chunk
&emsp;
* 闪银石&emsp;sivite
	［备注］原为天蓝石 lazulite，找不到引用，暂且这样翻译
* 心印石&emsp;Koanite
	［引用］koan：以心传心。原为磷酸铝。（名字起得这么好，却只是用来生产磷？）
&emsp;
* 佩格拉希合金&emsp;Peglaci Alloy
&emsp;
* 特勒贝晶体碎片&emsp;Telebrium
	［生成］特勒贝晶体&emsp;Telebrium Bar
* 月晶碎片&emsp;Lunari Shard
	［生成］月晶&emsp;Lunari Crystal
	［引用］Luna：月之女神
* 镭矿&emsp;Irradium Ore
	［生成］镭锭&emsp;Irradium Bar
* 混乱原生质，腐化原生质&emsp;Lasombrium
	［生成］混乱原生质之种，腐化根源&emsp;Lasombrium Seed
* 高熔点矿&emsp;Zerchesium
	［生成］高熔点锭&emsp;Zerchesium Bar
* 原体矿&emsp;Protocite Ore
	［生成］原体锭&emsp;Protocite Bar
	［引用］Proto：原型。
* 半影矿&emsp;Penumbrite Ore
	［生成］半影碎片，半影锭，&emsp;Penumbrite Shard
	［引用］penumbra：半影
* 棱镜碎片&emsp;Prisillite Ore?
	［生成］棱镜之星&emsp;Prisillite Star
* 原力矿&emsp;Trianglium
	［生成］原力棱锥，原力锭，原力金字塔&emsp;Trianglium Pyramid
	［引用］Triangle：三角形，Pyramid：金字塔，棱锥
* 寂灭矿&emsp;Quietus Ore
	［生成］寂灭锭&emsp;Quietus Bar
	［引用］Quietus：寂灭，生命的终止
* 寒霜矿&emsp;Isogen Ore
	［生成］寒霜锭&emsp;Isogen Bar
	［引用］Isogen：等角多边形
* 永燃矿&emsp;Pyreite Ore
	［生成］永燃锭&emsp;Pyreite Bar
	［引用］Pyre：火葬柴堆
* 赛德瑞瑟晶体碎片&emsp;Xithricite Ore
	［生成］赛德瑞瑟晶体&emsp;Xithricite
* 幻影矿&emsp;Effigium Ore
	［生成］幻影锭&emsp;Effigium Bar
	［引用］Effigy：肖像，模拟像，仿真像
* 超致密矿&emsp;Densinium Ore
	［生成］超致密锭&emsp;Densinium Bar
	［引用］Dense：致密的
* 诺克原石&emsp;Raw Nocxium
	［生成］诺克石锭&emsp;Nocxium Bar
	［引用］出自EVE，超新星诺克石。

### 合金

* 异极合金&emsp;Morphite
	［生成］异极合金锭&emsp;Morphite Bar
* 高级合金&emsp;Advanced Alloy
* 超钛锭，三钛合金&emsp;Tritanium Bar
	［引用］出自EVE，一种非常坚硬但有韧性的金属，但在大气温度下不稳定。
* 致密合金&emsp;Dense Alloy
	［引用］Dense：致密的
* 阳清合金&emsp;Aetherium Alloy
	［引用］可能出自上古卷轴，来自光界的物质碎片。Aether：以太。

### 放射性

**原版**

* 钚&emsp;Plutonium Ore
	［生成］钚棒&emsp;Plutonium Rod
* 铀&emsp&emsp;Uranium Ore
	［生成］铀棒&emsp;Uranium Rod

**FU**

* 氘棒(2H)&emsp;Deuterium (2H)
* 氚棒(3H)&emsp;Tritium (3H)
* 浓缩钚棒(Pu)&emsp;Enriched Plutonium (Pu)
* 浓缩铀棒(U)&emsp;Enriched Uranium (U)
* 镎(Np)&emsp;Neptunium (Np)
	［生成］镎棒(Np)&emsp;Neptunium Rod (Np)
* 钍(Th)&emsp;Thorium (Th)
	［生成］钍棒(Th)&emsp;Thorium Rod (Th)
&emsp;
* 奥创棒(Ux3)&emsp;Ultronium(Ux3)
	［引用］Ultro：奥创，美国漫威漫画旗下超级反派。
&emsp;
* 中子素 (Nu)&emsp;Neutronium (Nu)
* 反中子素 (Nux2)&emsp;Anti-Neutronium (Nu)

### 半龙人水晶

* 天使石水晶（已删除）&emsp;Angelite Crystal
	［备注］泪珠状，摸起来有点冷
&emsp;
* 欧普尔水晶&emsp;Opul Crystal
	［备注］温暖，治愈
* 艾米拉水晶&emsp;Emera Crystal
	［引用］祖母绿：Emerald
	［备注］成群生长，非常脆弱
* 菲亚水晶&emsp;Feya Crystal
	［备注］黯淡，几乎不发光
* 柯斯帕水晶&emsp;Kespar Crystal
	［备注］在阳光下闪闪发光
* 大洋石水晶&emsp;Oceanite Crystal
	［引用］Ocean：海洋
* 瑞吉特水晶&emsp;Rekite Crystal 
	［备注］提供极少量的燃料
* 心叶石水晶&emsp;Thantite Crystal
	［引用］Thanat：死亡学，死因学，死神
	［备注］生长在不同寻常之处  
&emsp;  
* 纳德&emsp;Nhydri

### 液体

**原版**

* 水&emsp;Water
* 生命之泉&emsp;Healing Water
* 岩浆&emsp;Lav
* 咖啡&emsp;Liquid Coffee？？
* 椰奶&emsp;Milk？？
* 油&emsp;Oil
* 毒液&emsp;Poison Water？
* 黏液&emsp;Slime
* 沼泽水&emsp;Swamp Water
&emsp;
* 液态能源 -> 厄尔吉斯液态燃料

**FU**

* 厄尔吉斯液态燃料&emsp;liquid fuel
* 外星汁液，未知之水&emsp;Alien Juice
* 腐化之水，黑暗之水&emsp;Dark Water
* 汞&emsp;Mercury
* 纯蜂蜜&emsp;Pure Honey
* 氦-3&emsp;Helium-3
* 以太&emsp;Aether
* 纯啤酒&emsp;Beer
* 生物软泥&emsp;Bio-Ooze
* 焦油&emsp;Black Tar
* 血液&emsp;Blood
* 液化水晶&emsp;Liquified Crystal
* 液态氘&emsp;Liquid Deuterium
* 远古液&emsp;Elder Fluid
* 重力液体&emsp;Grav-Liquid
* 橙色重力液体&emsp;Orange Grav-Liquid
* 液态铁&emsp;Liquid Iron
* 液态镭&emsp;Liquid Irradium
* 液态汞&emsp;Liquid Mercury
* 液态金属氢&emsp;Liquid Metallic Hydrogen
* 液氮&emsp;Liquid Nitrogen
* 有机液，有机汤&emsp;Organic Soup
* 脓液&emsp;Pus
* 硫酸&emsp;Sulphuric Acid
* 污染水&emsp;Contaminated Water
* 暗影气体&emsp;Shadow Gas
* 原体液&emsp;Liquid Protocite

### 设备

## 状态（按照目录）（不包括动画文本）（不包括单纯的能力值调整效果）

### ［原版状态］

* 燃烧&emsp;Beam Burning
* 休息 Lv.1 ~ 休息 Lv.6&emsp;Bed 1 ~ Bed 6
* 致命严寒&emsp;biome cold
* 致命酷热&emsp;biome heat
* 致命辐射&emsp;biome radiation
* 弹性&emsp;bouncy
* 燃烧&emsp;burning
* 伪装 Lv.1 ~Lv.5&emsp;camouflage0 & 25 & 34 & 50 75
* 崩溃&emsp;crash
* 殒灭&emsp;doomed
* 抗电&emsp;electric Block
* 带电&emsp;electrified
* 能量再生&emsp;energy regen
* 受惊&emsp;erchiussickness
* 抗火&emsp;burn spray
* 防火&emsp;fire Block
* 饥饿&emsp;hungry
* 饥极&emsp;starving
* 饱腹&emsp;well fed
* 食物中毒&emsp;food poison
* 减速&emsp;frost slow
* 减速&emsp;frost snare
* 发光&emsp;glow
* 发光&emsp;ship glow
&emsp;
* 治疗 Lv.2&emsp;bandage heal
	［来源］绷带
* 治疗 Lv.1&emsp;bottled water heal？？
* 治疗 Lv.3&emsp;medkit heal
	［来源］医疗包
* 治疗 Lv.3&emsp;nanowrap heal
	［来源］纳米绷带
* 治疗 Lv.2&emsp;salve heal&emsp;［来源］药膏
&emsp;
* 抗寒&emsp;ice block
* 隐形&emsp;invisble
&emsp;
* 跳跃增强 Lv.2&emsp;jump boost
* 跳跃增强 Lv.1&emsp;jump boost 20
* 跳跃增强 Lv.1&emsp;jump boost food
* 跳跃增强 Lv.2&emsp;ship jump boost
&emsp;
* 伤害提升&emsp;large damage boost
* 悬浮&emsp;levitation
* 轻盈&emsp;low grav
* 轻盈&emsp;staff low grav
&emsp;
* 熔化&emsp;melting
* 减速&emsp;mud slow
* 安全下落&emsp;no fall damage
* 赤裸&emsp;nude
* 过载&emsp;overload
* 麻痹&emsp;paralysis
&emsp;
* 沙暴&emsp;sandstorm
* 减速&emsp;slime slow
* 减速&emsp;staff Slow
* 减速&emsp;stun&emsp;晕眩
* 减速&emsp;tar slow
&emsp;
* 荆棘&emsp;enemy nova
* 荆棘&emsp;nova
* 荆棘&emsp;thorns
&emsp;
* 中毒&emsp;weak poison
* 潮湿&emsp;wet
* 逆风&emsp;wind swept

### 护甲效果：fu_armoreffects

* 免疫 - 极端寒冷&emsp;Cold Shield
	`stats/effects/fu_armoreffects/ffextremecoldresist`
* 免疫 - 极端炎热&emsp;Heat Shld
	`stats/effects/fu_armoreffects/ffextremeheatresist`
* 免疫 - 极端辐射&emsp;Rad Shld
	`stats/effects/fu_armoreffects/ffextremeradiationresist`
* 壁垒&emsp;Barrier
	`stats/effects/fu_armoreffects/movementprotection`
* 防御&emsp;Defense
	`stats/effects/fu_armoreffects/quietuseffects`
* 分隔&emsp;Spacer
	`stats/effects/fu_armoreffects/spacefarerimmunity`

### 未归类：fu_effects

* 蛰伤&emsp;Sting
	`stats/effects/fu_effects/beesting/beesting & fubeesting/2/3/4`
* 重启&emsp;Reboot
	`stats/effects/fu_effects/brainreboot/brainreboot`
* 不会被黏&emsp;No Stick
	`stats/effects/fu_effects/corvexputty/corvexputty`
* 暴击伤害+&emsp;Crit Dmg+
	`stats/effects/fu_effects/critbonus/critbonus1`
* 暴击几率+&emsp;Crit %+
	`stats/effects/fu_effects/critbonus/critchance1 & 2`
* 耗尽&emsp;Drain
	`stats/effects/fu_effects/drain/drain`
* 自我吞噬&emsp;Self-Cannabalism
	`stats/effects/fu_effects/eatself/eatself`
* 熵光护卫&emsp;Entropic Warding
	`stats/effects/fu_effects/entropicward/myphisfx`
* 触手缠身&emsp;Tentacle Debuff
	`stats/effects/fu_effects/entropicward/tentacleeffect`
* 扎根&emsp;Rooted
	`stats/effects/fu_effects/freeze/rootfu.`
* 冻住&emsp;Frozen
	`stats/effects/fu_effects/freeze/freeze /freenzefu/freezefu2`
* 霜灼&emsp;frozenburning
	`stats/effects/fu_effects/frozenburning/frozenburning`
* 弹力&emsp;Bounce
	`stats/effects/fu_effects/fu_medicine/bouncy/fubouncy`
* 恶魔契约 - 增加速度，伤害和抗性。降低生命和能量。持续2分钟。&emsp;Devils Bargain - Increases speed, damage and resistances. Saps health and energy. 2 minute duration.
	`stats/effects/fu_effects/fu_medicine/devilsbargain/devilsbargain`
* 发光&emsp;Glow
	`stats/effects/fu_effects/glow/glowblue &2 glowgreen &2 gloworange &glowpurple & 2 & glowred & glowyellow &2 &portablelightsource & ultraglow`
* 幸运&emsp;Luck
	`stats/effects/fu_effects/goldmead/goldmead`
* 醉酒&emsp;Intoxicated
	`stats/effects/fu_effects/intoxicated/booze & & 3`
* 魔法护盾&emsp;Mage Shield
	`stats/effects/fu_effects/mage_shield/mage_shield_lvl1 & mage_shield_lvl1shadowcrab & mage_shield_lvl4 & mage_shield_lvl4starspawn`
* D-盾&emsp;D-Shield
	`stats/effects/fu_effects/mage_shield/wretchelshield`
* 某些东西正在你的皮肤下孕育着。&emsp;Something is gestating under your skin.
	`stats/effects/fu_effects/popmead/larvalmead`
* 你可以闻到宇宙的味道——这一切。&emsp;You can smell the universe. All of it.
	`stats/effects/fu_effects/radiendirt/radiendirt`
* 恍恍惚惚红红火火&emsp;Trololololol
	`stats/effects/fu_effects/trolol/trolol`

### 免疫效果：fu_immunityeffects

* 免疫 - 蜂蜇&emsp;X-Sting
	`stats/effects/fu_immunityeffects/beestingimmunity`
* 免疫 - 精神错乱和黑暗&emsp;Immunity - Insanity and Darkness
	`stats/effects/fu_immunityeffects/darklightimmunity`
* 免疫 - 黑暗&emsp;Immunity - Darkness
	`stats/effects/fu_immunityeffects/darknessimmunity`
* 免疫 - 能源幽灵&emsp;Ghostproof
	`stats/effects/fu_immunityeffects/erchiusimmunity`
* 过量蜂蜜&emsp;Too much Honey
	`stats/effects/fu_immunityeffects/fedhoney`
* 免疫 - 致命严寒&emsp;X-Cold Shield
	`stats/effects/fu_immunityeffects/ffextremecoldimmunityicon`
* 免疫 - 致命炎热&emsp;X-Heat Shld
	`stats/effects/fu_immunityeffects/ffextremeheatimmunityicon`
* 免疫 - 致命辐射&emsp;X-Rad Shield
	`stats/effects/fu_immunityeffects/ffextremeradiationimmunityicon`
* 免疫所有 - 重力雨&emsp;X-Grav
	`stats/effects/fu_immunityeffects/gravrainimmunity`
* 免疫 - 精神错乱&emsp;Immunity - Insanity
	`stats/effects/fu_immunityeffects/insanityimmunity`
* 免疫 - 脓液&emsp;Pus Proof
	`stats/effects/fu_immunityeffects/pusimmunity`
* 免疫 - 辐射&emsp;Rad Shield
	`stats/effects/fu_immunityeffects/radiationimmunityicon`
* 免疫 - 暗影&emsp;Immunity - Shadow
	`stats/effects/fu_immunityeffects/shadowimmunity`
* 免疫 - 毒&emsp;Immunity - Poison
	`stats/effects/fu_immunityeffects/poisonimmunity & poisonimmunitycrystal & poisonimmunityspongeweed`

### 物块效果：fu_tileeffects

* 暗影气体 - 被暗影抗性抵抗。&emsp;Shadow Gas. Resisted by Shadow resistance.
	`stats/effects/fu_tileeffects/gas_effects/shadowgas/shadowgasfx`
&emsp;
* 高重力事件 (重力+50%) &emsp;High Gravity Event (+50% Gravity)
	`stats/effects/fu_tileeffects/gravity_effects/gravrain/mountainmass`
* 橙色重力雨&emsp;Orange Gravity Rain
	`stats/effects/fu_tileeffects/gravity_effects/gravrain/orangegravrain.statuseffect`"
&emsp;
* 减速 (黏土) &emsp;Slow (Clay)
	`stats/effects/fu_tileeffects/mobility_effects/fuclayslow`
* 减速 (泥) &emsp;Slow (Clay)
	`stats/effects/fu_tileeffects/mobility_effects/fuclayslow.`
* 减速 (丛林) &emsp;Slow (Jungle)
	`stats/effects/fu_tileeffects/mobility_effects/jungleslow`
* 流沙&emsp;Quicksand
	`stats/effects/fu_tileeffects/mobility_effects/fuquicksand`
&emsp;
* 中血毒！- 这种毒会持续很长很长的时间。&emsp;Blood Poisoned! - This poison will last a long, long time.
	`stats/effects/fu_tileeffects/poison_effects/biooozepoison/biooozepoisonlongterm`
* 软泥 - 被毒素抗性抵抗。&emsp;Oozed. Resisted by Poison resistance.
	`stats/effects/fu_tileeffects/poison_effects/biooozepoison/biooozepoison & 2 & biooozepoisonshort`
	［来源］生物软泥
* 恶心的毒 - 被毒素抗性抵抗。&emsp;Nasty Toxin.  Resisted by Poison resistance.
	`stats/effects/fu_tileeffects/poison_effects/contaminatedpoison/contaminatedpoison`
* 腐化之毒 - 被毒素抗性抵抗。&emsp;Darkwater Poison.  Resisted by Poison resistance.
	`stats/effects/fu_tileeffects/poison_effects/darkwaterpoison/darkwaterpoison`
	［来源］腐化之水
* 紧急自杀装置！有担保的死亡！来自凯文科技的最新产品！&emsp;Killpod! Death, Guaranteed! New from Kevin-Tek!
	`stats/effects/fu_tileeffects/poison_effects/killpod/killpod`
* 汞毒 - 被毒素抗性和放射抗性抵抗。&emsp;Mercury Poison.  Resisted by Poison + Radioactive resistance.
	`stats/effects/fu_tileeffects/poison_effects/mercurypoison/mercurypoison`
	［来源］水银
* 灼热疼痛 - 被火炎抗性抵抗。&emsp;Scorching pain. Resisted by Fire resistance.
	`stats/effects/fu_tileeffects/poison_effects/moltenmetal/moltenmetal &2 &3`
* 致命寒意 - 被寒气抗性抵抗。&emsp;Deadly Chill. Resisted by Ice resistance.
	`stats/effects/fu_tileeffects/poison_effects/nitrogenfreeze/icethrowereffect & nitrogenfreeze & & 3`
	［来源］液氮，
* 呃，脓液 - 每下造成6点伤害。被物理抗性抵抗。&emsp;Eeew. Causes 6 damage per tick. Resisted by Physical resistance.
	`stats/effects/fu_tileeffects/poison_effects/pus/puseffect`
	［来源］脓液
* 辐射灼伤 - 被放射抗性抵抗。&emsp;Radiation Burn. Resisted by Radiation resistance.
	`stats/effects/fu_tileeffects/poison_effects/radiationburn/radiationburn`
	［来源］辐射土块，放射性废料，
* 修格斯腐蚀&emsp;Shoggoth Corrosion
	`stats/effects/fu_tileeffects/poison_effects/shoggothburn/shoggothburn`
	［来源］修格斯肉？？？
* 酸性灼伤 - 被物理抗性抵抗。&emsp;Acid Burn. Resisted by Physical resistance.
	`stats/effects/fu_tileeffects/poison_effects/sulphuricacideffect/sulphuricacideffect`
	［来源］硫酸土块？？
&emsp;
* 精神错乱&emsp;Insane&emsp;★★★
	`stats/effects/fu_tileeffects/specialty_effects/insanity/insanity & 2`
	［来源］阿托罗斯的一些物块？
* 消极瘴气。-阻碍压强保护和治疗。&emsp;Negative Miasma - Blocks pressure protection and healing
	`stats/effects/fu_tileeffects/specialty_effects/negativemiasma/negativemiasma`
* 有机液 - 回复饥饿值。&emsp;Organic Soup - Restores hunger
	`stats/effects/fu_tileeffects/specialty_effects/organicsoupeffect/organicsoupeffect`
	［来源］有机液
* 被黏住&emsp;Slimed
	`stats/effects/fu_tileeffects/specialty_effects/slimefriction/slimefriction`
	［来源］黏液
* 粘泥&emsp;Sticky Slime
	`stats/effects/fu_tileeffects/specialty_effects/slimestick/slimestick`
* 不可破坏的黑暗&emsp;Unbreachable Darkness&emsp;★★★
	`stats/effects/fu_tileeffects/specialty_effects/superdark/superdarkstat.statuseffect`
	`stats/effects/fu_tileeffects/specialty_effects/superdark/superdarkstatUnblockable.statuseffect`
	`stats/effects/fu_tileeffects/specialty_effects/superdark/superdarkstatlarge.statuseffect`
	`stats/effects/fu_tileeffects/specialty_effects/superdark/superdarkstatmid.statuseffect`
	`stats/effects/fu_tileeffects/specialty_effects/superdark/superdarkstatshoggoth.statuseffect`"
* 粘网&emsp;Sticky Webs
	`stats/effects/fu_tileeffects/specialty_effects/webstick/webstick & ...grappler`
	［来源］蜘蛛网？？
* 狂风&emsp;Windy&emsp;★★
	`stats/effects/fu_tileeffects/specialty_effects/windslow/windslow`
* 暗影污染&emsp;Shadow Tainted&emsp;★★★
	`stats/effects/fu_tileeffects/specialty_effects/darkstalker/darkstalker & ...Unblockable`
	`stats/effects/fu_tileeffects/specialty_effects/insanityblur/insanityblurstat.animation？？？`
	`stats/effects/fu_tileeffects/specialty_effects/superdark/superdarkstat.animation？？？`
* 蜂蜜&emsp;Honey
	`stats/effects/fu_tileeffects/mobility_effects/honeyslow & 2`
	［来源］纯蜂蜜

### 武器效果：fu_weaponeffects

* 轻微出血&emsp;Light Bleeding
	`stats/effects/fu_weaponeffects/bleeding/bleeding05.statuseffect`
* 大出血&emsp;Profuse Bleeding
	`stats/effects/fu_weaponeffects/bleeding/bleedinglong2.statuseffect`
* 出血&emsp;Bleeding
	`stats/effects/fu_weaponeffects/bleeding/bleedinglong & ...hunter & ...short`
* 凝固&emsp;Napalm&emsp;★★★
	`stats/effects/fu_weaponeffects/burningnapalm/burningnapalm`
* 燃烧&emsp;Burn&emsp;★★★
	`stats/effects/fu_weaponeffects/firelight/firelight`
* 重力枪&emsp;Grav Gun
	`stats/effects/fu_weaponeffects/gravgun/gravgun`
* 无能狂怒&emsp;Dunce Rage
	`stats/effects/fu_weaponeffects/Skittles/marvinSkittles`
* 群体冻结&emsp;Greg Freeze
	`stats/effects/fu_weaponeffects/Skittles/timefreezeSkittles`
* 精准射击&emsp;Pistol Accuracy
	`stats/effects/fu_weaponeffects/swashbucklerpower`

### 环境效果：fu_weathereffects

* 致死严寒&emsp;Lethal Cold
	`stats/effects/fu_weathereffects/ffextremecold/ffextremecold`
* 致死辐射&emsp;Lethal Radiation
	`stats/effects/fu_weathereffects/ffextremeradiation/ffextremeradiation`
* 致死酸蚀&emsp;Acid
	`stats/effects/fu_weathereffects/ffextremesulphuric/ffextremesulphuric`
&emsp;
* 压强&emsp;Pressure
	`stats/effects/fu_weathereffects/gasworld/gasworldweak`
* 重度压强&emsp;Severe Pressure
	`stats/effects/fu_weathereffects/new/gasworldnew/gasworld2`
* 极高压强&emsp;High Pressure
	`stats/effects/fu_weathereffects/new/gasworldnew/gasworld1`
&emsp;
* 致死压强&emsp;Lethal Pressure
	`stats/effects/fu_weathereffects/gasworld/gasworld`
	`stats/effects/fu_weathereffects/new/gasworldnew/gasworld3`
&emsp;
* 以太大气&emsp;Aetheric Atmosphere
	`stats/effects/fu_weathereffects/new/aether/aetherweathernew`
	［备注］降低能量
* 极端以太&emsp;Extreme Aether
	`stats/effects/fu_weathereffects/new/aether/aetherweathernew2`
* 致命以太&emsp;Deadly Aether
	`stats/effects/fu_weathereffects/new/aether/aetherweathernew3`
&emsp;
* 重度寒冷&emsp;Severe Cold
	`stats/effects/fu_weathereffects/new/cold/ffbiomecold1.statuseffect`
* 极端寒冷&emsp;Extreme Cold
* 致命严寒&emsp;Deadly Cold
&emsp;
* 冻结&emsp;Freezing
	`stats/effects/fu_weathereffects/new/cold/coldweathernew.statuseffect`
* 寒流 I & II & III&emsp;Cold Snap & II & III
	`stats/effects/fu_weathereffects/new/cold/suddenchill1.statuseffect & 2 & 3`
&emsp;
* 沙漠炎热&emsp;Desert Heat
	`stats/effects/fu_weathereffects/new/desert/desertweathernew`
* 致命沙漠炎热&emsp;Deadly Desert Heat
	`stats/effects/fu_weathereffects/new/desert/desertweathernewdeadly`	
* 热浪 I & II & III&emsp;Heatwave & II & III
	`stats/effects/fu_weathereffects/new/desert/heatwave1 & 2 & 3`
&emsp;
* 雷电风暴&emsp;Electrical Storm
	`stats/effects/fu_weathereffects/new/electric/ffbiomeelectric1`
* 重度雷电风暴&emsp;Severe Electrical Storm
* 致命雷电风暴&emsp;Deadly Electrical Storm
&emsp;
* 重度炎热&emsp;Severe Heat
	`stats/effects/fu_weathereffects/new/heat/ffbiomeheat1`
* 极端炎热&emsp;Extreme Heat
&emsp;
* 重度的毒&emsp;Severe Poison
	`stats/effects/fu_weathereffects/new/poison/biomepoison1`
* 极端的毒&emsp;Extreme Poison
* 致命的毒&emsp;Deadly Poison
* 猛毒气体&emsp;Severe Poison Gas
	`stats/effects/fu_weathereffects/new/poison/biomepoisongas`
* 毒&emsp;Poison
	`stats/effects/fu_weathereffects/new/poison/poisonweathernew`
	`stats/effects/fu_weathereffects/new/poison/poisonweathernewbiome`
&emsp;
* 原毒&emsp;Proto Poison
	`stats/effects/fu_weathereffects/new/protoworld/protoweather`
* 重度原毒&emsp;Severe Proto Poison
&emsp;
* 重度辐射&emsp;Severe Radiation
	`stats/effects/fu_weathereffects/new/radiation/radioactiveweathernew`
* 极端辐射&emsp;Extreme Radiation
* 致命辐射&emsp;Deadly Radiation
&emsp;
* 重度酸蚀&emsp;Severe Acid
	`stats/effects/fu_weathereffects/new/sulphuric/sulphuricweathernew`
* 致命酸蚀&emsp;Deadly Acid
* 不可理喻的酸蚀&emsp;Brutal Acid
* 不可想象的酸蚀&emsp;Impossibly Acidic
&emsp;
* 酸性风暴&emsp;Acid Storm
	`stats/effects/fu_weathereffects/new/sulphuric/sulphuricweatherstorm`
* 致命酸性风暴&emsp;Deadly Acid Storm
* 不可想象的酸性风暴&emsp;Impossible Acid Storm
&emsp;
* 热带炎热&emsp;Tropical Heat
	`stats/effects/fu_weathereffects/new/tropical/jungleheatweather`
&emsp;
* 中毒&emsp;Poisoned
	`stats/effects/fu_weathereffects/metallichydrogengas/metallichydrogengas`
	`stats/effects/fu_weathereffects/metallichydrogengas/metallichydrogenliquid`
	`stats/effects/fu_weathereffects/poisongas/poisongas`
	［来源］金属氢，液态金属氢，有毒气体
&emsp;
* 伤害降低&emsp;Sap Dmg
	`stats/effects/fu_weathereffects/weakenworld/weakenweather & 2`
* 未知生物群系&emsp;Unknown Biome
	`stats/effects/fu_weathereffects/unknownbiomeeffect`

### 根目录

* 免疫气体&emsp;X-Gas
	`stats/effects/liquidimmunity/gasimmunity.statuseffect`
* 沉重&emsp;Heavy
	`stats/effects/lowgrav/lowgrav_supergrav.statuseffect`
* 反重力力场&emsp;Reverse-Grav Field
	`stats/effects/lowgrav/lowgrav_wretchel.statuseffect`
* 轻盈&emsp;Light
	`stats/effects/lowgrav/lowgrav_intrepid.statuseffect`
	`stats/effects/lowgrav/lowgrav_stim.statuseffect`
* 漂浮&emsp;Float
	`stats/effects/lowgrav/lowgrav_fallspeed.statuseffect`
	`stats/effects/lowgrav/lowgrav_fallspeedup.statuseffect`
* 低重力&emsp;Low Gravity
	`stats/effects/lowgrav/lowgrav_neutronmagnorb.statuseffect`
	`stats/effects/lowgrav/lowgrav_shadowmagnorb.statuseffect`

### 药物效果：medicalStationSpecials（orange）

* 狂怒&emsp;Berserks Rage
	`stats/effects/medicalStationSpecials/berserk/berserk`
* 试验 #322&emsp;Experiment #322
	`stats/effects/medicalStationSpecials/experimental/experimental`
* 玻璃大炮&emsp;Glass Cannon
	`stats/effects/medicalStationSpecials/glasscannon/glasscannon`
* 蜂群思维&emsp;Hivemind
	`stats/effects/medicalStationSpecials/hivemind/hivemind`
* 狂躁&emsp;Hypopanic
	`stats/effects/medicalStationSpecials/hypopanic/hypopanic.statuseffect`
* 免疫&emsp;Immunization
	`stats/effects/medicalStationSpecials/immunization/immunization.`
* 重型卡车&emsp;Juggernaut
	`stats/effects/medicalStationSpecials/juggernaut/juggernaut.statuseffect`
* 线粒体&emsp;Mitochondria
	`stats/effects/medicalStationSpecials/mitochondria/mitochondria.statuseffect`
* 情绪兴奋剂&emsp;Renergizer
	`stats/effects/medicalStationSpecials/renergizer/renergizer.statuseffect`
* 毒云&emsp;Toxic Cloud
	`stats/effects/medicalStationSpecials/toxiccloud/toxiccloud.statuseffect`
* 巨魔血&emsp;Trollblood
	`stats/effects/medicalStationSpecials/trollblood/trollblood.statuseffect`

### 回复效果：regeneration

* 日光疗愈&emsp;Daylight Regen
	`stats/effects/regeneration/lightregen.statuseffect`
* 黑夜疗愈&emsp;Darkheal
	`stats/effects/regeneration/darkregen`
	`stats/effects/regeneration/darkregenproduce`
* 日光疗愈&emsp;Lightheal
	`stats/effects/regeneration/lightregenenergy`
	`stats/effects/regeneration/lightregenproduce`
&emsp;
* 再生&emsp;Regeneration
	`stats/effects/regeneration/precursorregeneration.statuseffect`"
* 中等生命回复&emsp;Average Regen
	`stats/effects/regeneration/regeneration2.statuseffect`"
* 生命回复 Lv.1&emsp;Regen
	`stats/effects/regeneration/regenerationblock.statuseffect`
* 略微生命回复&emsp;Minimal Regen
	`stats/effects/regeneration/regenerationminor000.statuseffect`
* 弱效生命回复 II&emsp;Minor Regen II
	`stats/effects/regeneration/regenerationminor2.statuseffect`
* 生命回复 II&emsp;Regen II
	`stats/effects/regeneration/regenerationminor2augment.statuseffect`
* 生命回复 III&emsp;Regen III
	`stats/effects/regeneration/regenerationminor3augment.statuseffect`"
* 弱效生命回复 (EPP插件) &emsp;Augment Regen - Minor
	`stats/effects/regeneration/regenerationminoraugment.statuseffect`
* 细胞再生&emsp;Cellular Regeneration
	`stats/effects/regeneration/regenerationminorcellular.statuseffect`
* 奇迹草生命回复
	`stats/effects/regeneration/regenerationmiraclegrass.statuseffect`
* 生命值低于60%时，生命回复速度+8%&emsp;Regen +8% when below 60% health
	`stats/effects/regeneration/regenerationsanguine.statuseffect`
* 高效生命回复&emsp;High Regen
	`stats/effects/regeneration/regeneration3 & 4 & 5`
	`stats/effects/regeneration/regenmomma`
* 弱效生命回复 Lv.1&emsp;Minor Regen
	`stats/effects/regeneration/regeneration01`
	`stats/effects/regeneration/regenerationminor`
&emsp;
* 次等生命回复&emsp;Lesser Regen
	`stats/effects/regeneration/regenerationminor3`
	`stats/effects/regeneration/regenerationmommatop`

### 根目录

* 感电&emsp;Electrified
	`stats/effects/slimeleech/slimeleech`

### 反伤

* 幽灵瘴气&emsp;Ghostly Miasma
	`stats/effects/thorns/ghostburst`
* 新星&emsp;Nova
	`stats/effects/thorns/novax10`
* 元素反伤&emsp;Flame
	`stats/effects/thorns/fireburst`
	`stats/effects/thorns/fireburstmonster`
	`stats/effects/thorns/iceburst`
* 反伤&emsp;Thorns
	`stats/effects/thorns/burstfayshroom`
	`stats/effects/thorns/thornsstranglevine`
	`stats/effects/thorns/thornsstranglevinesuper`

### 根目录

* 时间冻结&emsp;Time Freeze
	`stats/effects/timefreeze/timefreeze2`
	`stats/effects/timefreeze/timefreezeNoVFX`
&emsp;
* 潮湿&emsp;Wet
	`stats/effects/wet/wet.statuseffect`
&emsp;
* 易伤&emsp;Vulnerable
	`stats/effects/extramodvulnerability`
* 寒冷&emsp;Cold
	`stats/effects/fu_weathereffects/crystalmoon/crystalmoonfx`
	`stats/effects/fu_weathereffects/new/cold/ffbiomecold0`
* 致命炎热&emsp;Deadly Heat
	`stats/effects/fu_weathereffects/ffextremeheat/cultistblastfx`
	`stats/effects/fu_weathereffects/ffextremeheat/ffextremeheat`
	`stats/effects/fu_weathereffects/new/heat/ffbiomeheat3`
* 治疗中&emsp;Healing
	`stats/effects/fu_effects/bandage2/bandage2fu`
	`stats/effects/heal/slimedaggerheal`
* 减速&emsp;Slow
	`stats/effects/fu_tileeffects/mobility_effects/blacktarslow`
	`stats/effects/fu_tileeffects/mobility_effects/slushslow.statuseffect`"
	`stats/effects/fu_tileeffects/mobility_effects/snowslow`
	`stats/effects/slow/slow`
	`stats/effects/staffslow/staffslow2`

### ［常见状态］

* 燃烧&emsp;Burning, Burn
* 凝固&emsp;Napalm
* 冻结&emsp;Frozing, Freezing
* 霜灼&emsp;Frost Burn, frozen-fire
* 出血&emsp;Bleeding
* 易伤&emsp;Vulnerability
* 辐射烧伤&emsp;Radiation Burn, Rad-Burn,Radiation?
* 麻痹&emsp;paralysis
* 电击/晕眩/感电&emsp;Shock, Shocked&emsp;electrified?&emsp;（来自电击）
* 眩晕&emsp;Stun&emsp;（来自重击）
* 中毒&emsp;Poison
* 虚弱&emsp;weakening
* 蜂蜇&emsp;Stinging, Sting
* 反伤&emsp;Thorns
* 狂暴&emsp;Rage
* 精神错乱&emsp;
* 恐惧 & 狩猎&emsp;Terrified & Hunted&emsp;erchiussickness & 2
* 减速&emsp;Slow
* 滑行&emsp;Slide
* 防御下降&emsp;Defense reduction

## 种族

* 羽族&emsp;Avali
	［备注］众所周知。
* ？？？，瑞登&emsp;Radien
	［备注］赛博朋克背景的种族。  
	［描述］一种奇怪的无机生物，由某种具有智能的放射性能量组成。
* ？？？，基霍斯&emsp;Kirhos
	［备注］善于交易。  
	［描述］这个啮齿类的种族耗尽了他们母星的自然资源。现在，他们大多居住在由企业运行的城市建筑中，而这些建筑被称为Arcologies。
* ？？？，佩格拉希&emsp;Peglaci
	［备注］发明了多种合金。  
	［描述］免疫寒冷和令人不快的事物。
* ？？？，曼提&emsp;Mantis
	［描述］繁殖快速，生命力顽强，Mantis既不聪明，也不讨人喜欢。
* ？？？，曼提斯&emsp;Mantizi
	［备注］硬皮肤，虫形，有一个帝国，专制。  
	［描述］外形像甲虫一样的杂食两足动物，拥有坚硬的几丁质外壳，充满活力，热爱自由。
* 影裔&emsp;Shadow
	［备注］非常神秘。
* ？？？，厄修安龙人，龙人&emsp;Eld'uukhar
	［备注］半龙，水晶工匠，基于水晶的科技。  
	［描述］Eld'uukhar会让人联想到传说中的巨龙。作为熟练的宝石和金属工匠，他们一边遨游宇宙，一边磨练自己的手艺。
* ？？？，瑟卢锡安&emsp;Thelusian
	［描述］他们是残忍而危险的战士，将自身的全部生命献给战斗、守卫以及其他枯燥的工作。单独一个Thelusian是极其不聪明的，但若组成大群体的话，效率便会变得非常高。
* ？？？，夏维克&emsp;Xarwiek&emsp;不可选
	［备注］非常罕见。
* ？？？&emsp;Tenebrhae&emsp;不可选
	［备注］...
* ？？？，阿诺德勒&emsp;anodyne
	［描述］Anodyne是一个形似“星际气囊”的神秘种族，很像星之子。他们既没有固定的定居点，也没有记录在案的历史。他们是一种不稳定的存在，不受过去的困扰。没有人知道他们由何构成，更没有人知道他们从何而来。
* 梦比斯&emsp;Myphis&emsp;darkizku
  	［描述］Myphis通常被认为是“可憎之物”。他们拥有异常强健的免疫系统，且是黑暗的追逐者。
* 伊库&emsp;Izku
	［描述］Izku几乎什么都不懂，他们的先进技术来自纯粹的幸运。
* 史莱姆&emsp;slimeperson
	［描述］当涉及到移民控制时，一些政府官员似乎完全没有注意到史莱姆们的存在。
* 夜种&emsp;Nightar
  	［描述］谜一般的夜种一族是在半影世界中进化而来的，深陷于传统的泥沼之中。他们充满自豪感，但是极端排外。
* 先驱者&emsp;Precursor
	［描述］残酷无情，诡计多端。
* 蜘蛛机器人&emsp;spiderdroid
	［描述］一种非常危险的机器人。

## NPC

### 前哨站

* 凯文 桑萨塔克&emsp;Kevin Sanchatak
	［备注］FU中最强NPC。
* 格雷格&emsp;Greg
	［备注］由凯文带回科学前哨站，Greg！
* 德雷克&emsp;Dereck
	［备注］...
* 卡尔，帽子爱好者&emsp;Carl,the hat enthusiast
	［备注］凯文的好朋友，羊驼
* 莱斯利博士&emsp;Dr. Lesley
	［备注］...
* 尼尔森博士&emsp;Dr. Nilson
	［备注］...
* 维纳利斯&emsp;Vinalisj
	［备注］初始星球的那只大猫，科学前哨站的主任。
* 赛迪西克斯&emsp;Xiticix
	［备注］科学前哨站的安全官。
* 史蒂夫&emsp;Steve
	［备注］试图通过自杀摆脱凯文，但是未能成功。
* 麦克雷迪&emsp;MacReady
	［备注］凯文的好朋友，显然不是正常人。
* 霍莉丝&emsp;Holix
	［备注］...
* 阿克希娜&emsp;Axiena
	［备注］燃料专家，翼族，哑巴。
* 贝拉&emsp;Bella
	［备注］...
* 硅宾&emsp;SILENES
	［备注］前哨站商人之一。

### 其他

* 泽尔迪亚&emsp;Zeldia
	［备注］有张肖像画。
* 岚&emsp;Ran
	［备注］银河Nightar商人。
* 戴夫&emsp;Dave
	［备注］备注对凯文来说意味这什么，对Mantizi族来说很是忌讳。

### 背景

* 奥拉纳&emsp;Orana
	［备注］Radien族的神祗，可能是FU世界观的创造神。
* 唯一者&emsp;The One
	［备注］对于影裔（Shadow）来说意味着什么。

## 怪物

* 死亡主宰 & 死亡主宰幼崽&emsp;ixo & ixoling
	［备注］原版怪物，叶族副本中的那种怪物。
* 吐舌娃&emsp;poptop,Xxxtop
	［备注］原版怪物，StarBound吉祥物，会唱歌，子分类很多。
* 血肉收割者&emsp;Fleshreaper
	［备注］...
* ？？？&emsp;Lilodon
	［备注］...
* ？？？&emsp;Anglure
	［备注］...
* ？？？&emsp;Bulbop
	［备注］...
* ？？？，（飞翼）豆荚&emsp;pteropod
	［备注］...
* Phantokat
* Chromingo
* Buggle
* spheretest
* Vile Snaunt
* Rimeling
* Spikespawn
* Rotter
* Scaveran Reptar
* Xxxxlit
* Ravager
* Narfin
* Xxxxflora
* Lilodon
* Glump
* Gloop
* Glarp
* golem&emsp;魔像

## 其他

* 尼克斯大浩劫&emsp;Nikos Point disaster
	［备注］Kirhos族的历史事件，这场浩劫导致了AI的全面禁止。
* 卡拉啤酒&emsp;Kahla Tankarad
	［备注］...
* 阿克恩&emsp;ArCon
	［备注］一支太空军队。
* ？？？&emsp;Fife
	［备注］...
* 瓦伊&emsp;Vai
	［备注］...
* 德拉瓦伊&emsp;Daravai
	［备注］...
* 泰克&emsp;Tek
	［备注］...
* CySol的私人娱乐网络&emsp;CySol's private entertainment network
	［备注］Kirhos族相关。
* 阿兹瑞尔工业&emsp;Azriel Industries
	［备注］...
* 水手凯尔普&emsp;Sailor Kelp
	［备注］鲛人漫画。
* ？？？&emsp;arcologies
	［备注］Kirhos族居住的集群建筑
* 科泰克星云&emsp;Kortakk nebula
	［备注］先驱相关
* ？？？&emsp;Chitron
	［备注］机甲相关，thelusian相关
* 新科公司&emsp;SinCo
	［备注］一家机甲公司
* 反异界？？？&emsp;Anti-Realm
* 德拉克&emsp;Drakaet
* 派克瑞特&emsp;Pykrete