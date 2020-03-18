	Created By 微风的龙骑士 风游迩 
	额外的参考文档（编写中）

#### 液体/附加状态/掉落物

* name
	* statusEffects
	* itemDrop
&emsp;
* alienjuice
	* swimming
	* liquidalienjuice
* beer
	* swimming,booze
	* liquidbeer
* bio_ooze
	* swimming,biooozepoison
	* liquidbioooze
* blacKtar&emsp;*不能游泳*
	* blacktarslow
	* liquidblacktar
* blood
	* swimming
	* liquidblood
* crystalliquid
	* swimming
	* liquidcrystal
* darkwater
	* swimming,darkwaterpoison
	* liquiddarkwater
* elderfluid
	* swimming,insanity
	* liquiderderfluid
* fuhoney
	* swimming,honeyslow
	* fu_liquildhoney
* fuhoneyred
	* swimming,honeyslow2
	* fu_liquildhoney
* fuironliquid
	* swimming,moltenmetal3
	* liquildironfu
* fuquicksand&emsp;*不能游泳*
	* fuquicksand
	* sand
* gravrain
	* swimming,gravrain
	* liquidgravrain
* helium3gas&emsp;*不能游泳*
	* helium3gasliquid
	* biomeairless,helium3gas
* hydrogengas&emsp;*不能游泳*，*气体*
	* biomeairless,gas
	* fu_hydrogen
* irradiumliquid
	* swimming,radioactivewathernew
	* liquidirradium
* liquidaether
	* swimming,aetherweathernew
	* liquidaether
* liquiddeuterium&emsp;液态氘&emsp;*不能游泳*
	* ？？？
	* liquiddeuterium
	* 燃料数值：5
* liquidnetrogen&emsp;*不能游泳*
	* nitrogenfreeze
	* liquidnetrogenitem
* mercuryliquid
	* swimming,mercurypoison
	* ff_mercury
* metallichydrogen
	* biomeairless,metallichydrogengas
	* fu_hydrogenmetallic
* funitrogengas&emsp;*气体*
	* biomeairless,gas
	* fu_nitrogen
* orangegravrain
	* swimming,orangegravrain
	* liquidorangegravrain
* organicsoup
	* swimming,organicsoupeffect
	* liquid organicsoup
* poisongas&emsp;毒气
	* biomeairless,poisongas,gas
	* liquidbiooze
* protociteliquid
	* swimming,energyregenfu20
	* vialproto
* pus
	* swimming,paseffect 
	* liquidpas
* shadowgas
	* shadowgasfx
	* shadowgasliquid
* sludge&emsp;污泥
	* swimming,wet
	* liquidwastewater
* sulphuricacid
	* swimming,sulphuricacid
	* liquidsulphuricacid
* wastewater
	* swimming,contaminatedpoison
	* liquidwastewater

#### 状态/效果

* burning&emsp;燃烧
	* 如果火炎抗性小于60，则每次造成6点基础火炎伤害。
* shocked&emsp;晕眩 = 感电
	* 每次造成12-20点电系伤害。默认持续5s。
* freeze = frozen = rooted&emsp;冻结
	* 眩晕效果，不同参数
* frozenburning&emsp;霜灼
	* groundMovement：.0.3，speed：0.75，airJump：0.85
	* 如果寒气抗性大于60/40/20，则每次造成3-2.5/1.75/1点寒气伤害。默认持续5s。
* fu_death&emsp;强制死亡
	* 每次造成88真实伤害。
&emsp;
* radiendirt&emsp;5克泥土
	* 如果是radien：booze3，slow，maxHP-20，持续240s
&emsp;
* wet&emsp;潮湿
	* run：90%，jump：90%
* waterwet&emsp;缓慢（水）
	* （鲛人族）run：130%，jump：130%&emsp;（叶族）run：120%，jump：120%&emsp;（其他）run：90%，jump：90%
&emsp;
* ......