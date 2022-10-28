# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 22:45:15 2022

@author: user
"""
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0,2550,256)
mtf_no_shift = [1,0.98783705818894063,0.96959097719774801,0.95192855637860141,0.93405812706029712,0.91643762163319265,0.89880642382178044,0.88134199170056426,0.86391965270207383,0.846634675254195,0.8294123493564417,0.81231317596553976,0.79528709736307934,0.77837592266786637,0.76154385432760385,0.74482159650326341,0.72818259613617342,0.71165098230210055,0.69520590898922596,0.67886781337636271,0.66261996000996082,0.64647935472295293,0.63043105015456902,0.61449008057690502,0.59864407801614727,0.58290818484044937,0.56727217476341119,0.55174963485403195,0.53632997545892058,0.52102558459723824,0.50582853162786667,0.49075293170682738,0.47579176001263113,0.46095522069192529,0.44623563202110073,0.43164706255926061,0.4171847541819439,0.4028584185906709,0.38866151671737148,0.37460811525728038,0.36069400065415225,0.34692679232581436,0.33330340924719543,0.31983852331787349,0.30652320627145951,0.2933706677200294,0.28038028942344512,0.26755910258992149,0.2549065222711428,0.24243547735974347,0.23013806683404495,0.21803238438783271,0.20610906222439493,0.19438599458376055,0.18285664143443012,0.17153897189280209,0.16042819571669992,0.14954291119423022,0.13887947549625138,0.12845625557692486,0.11827093435083194,0.10834283242989652,0.09867146843865382,0.089279637062166878,0.08016861728634822,0.071366528442624366,0.062875206875819933,0.054729300257239676,0.04693163993132702,0.039526228639764384,0.032520468891555701,0.025974011829706163,0.019899798172042182,0.014386929608368333,0.0094647396291977701,0.0052989994143720813,0.0019752825351620623,0.00013037150084969023,2.4256078438542455e-05,1.707121372271655e-05,9.5382397793315956e-06,1.0801826361505283e-05,2.9115912463490581e-06,3.8869468036948817e-06,2.9897975995765559e-06,1.9517343011851713e-06,6.834964106254457e-06,5.392559310857381e-06,8.6641760179968601e-06,6.4410892955256812e-06,8.071009091117134e-06,4.857926679843957e-06,4.8610594405653608e-06,5.5215939874339474e-07,1.0055554713644206e-06,6.4211091708802318e-06,9.413636756318918e-06,1.5856873653931326e-05,2.0090410546114163e-05,2.739542729945666e-05,3.2598163520484529e-05,4.0497619019600765e-05,4.6412321505691111e-05,5.744848382713713e-05,6.9635433124987231e-05,8.4555319317256846e-05,9.7157525235225462e-05,0.00010962494566159476,0.00011733444789474585,0.00012246866187366686,0.00012084224250391176,0.00011467356403999211,0.00010024233366601374,7.9858711260055051e-05,5.0273976096388305e-05,1.391170048537357e-05,3.2013232856737371e-05,8.4956933624264519e-05,0.0001472783107697451,0.00021631752164312114,0.00029405307634195664,0.00037773731102271578,0.00046902807066185166,0.00056511093753342651,0.00066737390520488422,0.00077297453707685169,0.00088308674517920203,0.00099488523300754169,0.0011093495176445942,0.0012236467035834518,0.0013388326630756017,0.0014522529165335856,0.0015647759316704927,0.0016738943969017244,0.0017803975086705614,0.0018819451632350404,0.0019793822451606644,0.0020704706432785268,0.0021561567848181942,0.002234423251498341,0.0023062188775247747,0.0023697793702092871,0.0024261837942843186,0.0024738189720090098,0.0025138616662328779,0.0025449738627755739,0.0025684167936242557,0.0025830285652442366,0.0025901782851351931,0.0025889567620556997,0.0025808156281161782,0.002565019730656115,0.0025430934067324973,0.0025144445921894266,0.0024798596665433922,0.0024400269297624112,0.0023982331469146194,0.0023540413642160747,0.0023091299960814114,0.0022630602687706029,0.0022174321425938257,0.0021718637749602136,0.0021278518656692577,0.00208504059899571,0.0020448163205195268,0.0020068405744791255,0.0019723708972096306,0.0019410763428685473,0.0019140685687048214,0.0018910217059094935,0.0018728799091604436,0.0018593351913863175,0.0018511392364938036,0.0018480270634517869,0.0018505256274475741,0.0018584568215458683,0.001872081399136787,0.0018914536411389633,0.0019167250001992364,0.0019426861299149344,0.0019336197483071846,0.0018979871461788267,0.0018555685921046439,0.0018021526878630103,0.0017402574882651165,0.0016674937587085954,0.0015862393846739588,0.0014951158867566349,0.0013965313650298745,0.0012897009369270864,0.0011770974822588988,0.0010583128224062298,0.00093584724814806629,0.00080952802228988414,0.00068182790839004545,0.00055267913766502059,0.00042448153774741999,0.00029718610223335379,0.00017305717696494989,5.1995592253626742e-05,6.3897173767583291e-05,0.00017483253599817844,0.00027889721417385824,0.00037645479303512262,0.00046581990608961666,0.00054758369398801899,0.00062048839377223301,0.00068521367881268429,0.00074048087635481495,0.00078717359336450516,0.00082427328909583672,0.00085282820913486484,0.00087200470771868412,0.00088299484467315727,0.00088515760840319211,0.00087983289355817471,0.00086652037797342488,0.00084665436032352304,0.00081987239596298877,0.00078770904521092554,0.00074987055971594506,0.00070794565736193114,0.00066172881482159506,0.00061282404498308669,0.00056104692532423178,0.00050803228828637194,0.00045358479283919522,0.00039932115884375288,0.00034504725090268954,0.00029236332773587714,0.00024109040323998604,0.00019307589840414772,0.0001475942595327864,0.00010525894614282807,6.5636245185965233e-05,2.9802100178417764e-05,2.815786505534827e-06,3.123210609284906e-05,5.6135553962587509e-05,7.664036624971835e-05,9.3539392225964408e-05,0.00010604554351025902,0.00011505260023924124,0.0001198689353912233,0.00012148518325791642,0.00011929687415662671,0.00011438781654868566,0.00010623148345573433,9.6002873924575481e-05,8.3253410547438043e-05,6.9263791174694434e-05,5.3665352541499203e-05,3.7894130200397867e-05,2.1678936485969526e-05,6.8297862477311089e-06,6.786624976620286e-06,]
mtf_500um = [1,0.98579421931628952,0.96379563782399014,0.94242527155587785,0.92088857224970488,0.89971963566660251,0.87859957198667571,0.85771257041659288,0.83689808034689106,0.81626940987324215,0.79574730006696515,0.77540783167391336,0.75518644776661259,0.73513193051227266,0.71520341837482926,0.69544355326520213,0.67581376372887147,0.65634790778406449,0.63701895122382068,0.61785741925851811,0.59884050573729797,0.57999253735147094,0.56129164315916724,0.54276594711567072,0.52439929474606639,0.50621364769905586,0.48819140747087375,0.4703580376330333,0.45270080864317125,0.43523847456259662,0.41796111612663445,0.40089235540241402,0.38401544638837065,0.36735567496139543,0.35090403515217222,0.33467753190291472,0.31866886917240406,0.30290029950264141,0.28735894565067299,0.27207144918607395,0.25702244091427562,0.24224110284922162,0.22771197865516604,0.21346391766268388,0.19948445504788614,0.18580150208590407,0.17240365415819486,0.1593211247701129,0.14654305799979284,0.13410289152235663,0.12199040177997104,0.11024324977126619,0.09885204138727198,0.087861058019959262,0.077262023104906818,0.067107992538316188,0.05739300804021203,0.048183894800940881,0.039477921107991691,0.031364393453062002,0.023847115332120156,0.017058245365315489,0.01101878617769351,0.0059711529007766334,0.0020234739508228784,0.00012323571546236071,4.3623193673747205e-05,2.3160434432595585e-05,3.9721483555150804e-05,2.3300786370822429e-05,3.2711385548150113e-05,2.143192623799527e-05,2.9801769473553198e-05,2.1974664539471276e-05,2.931593239627588e-05,2.4088432076401303e-05,3.1068463444062926e-05,2.7853325393267116e-05,3.4760501052747543e-05,3.3072058407816769e-05,3.9866468460887772e-05,3.8904304244190848e-05,4.4995643570507079e-05,4.376425079795449e-05,4.4267307826802624e-05,3.4536613127395449e-05,2.9315339551911615e-05,1.9530257941387126e-05,1.7800848176994533e-05,1.5947611435374941e-05,2.5148716705365636e-05,3.771349841586502e-05,6.3428160391170387e-05,9.4816815306211793e-05,0.00014037035939256864,0.00019268798607747952,0.00025907007578500872,0.00033218417994869317,0.00041830268944413444,0.00051013445884447303,0.00061307887884949001,0.00071994049862183769,0.00083541883880068179,0.00095248260792805484,0.0010752965795008133,0.001197076125650317,0.0013216095744210069,0.0014424343201432579,0.0015630831906662246,0.0016775102653984776,0.0017891040674296308,0.0018922654480761449,0.0019903626810780801,0.0020782578501041416,0.0021593929986156325,0.0022290623198367139,0.0022908617351773686,0.0023405630225200999,0.0023818065699775601,0.0024109064677085099,0.0024316107322722132,0.0024406160071060289,0.0024418107738010363,0.0024322861763228934,0.0024159592220945316,0.0023902951409573159,0.0023592689286728529,0.0023205752701854448,0.0022781443808860009,0.0022299069502303872,0.0021797618371631215,0.0021257612758898503,0.0020716428806616173,0.0020154718934966317,0.0019607604179487847,0.0019061548364619691,0.0018552266551369783,0.001806271867530141,0.0017626376631879636,0.0017226959080864608,0.0016894147578707136,0.0016611090451398205,0.0016404672569725232,0.0016259020251130183,0.0016197074388094759,0.0016205561031660655,0.001629844360810396,0.0016471875961736344,0.0016568795200365834,0.001620388759011192,0.0015664401182528338,0.0015024681180383591,0.001429481343363258,0.001345733350571255,0.0012526212968803204,0.0011486639182117927,0.0010367070446848786,0.00091591689684947209,0.00078962576647601337,0.00065737819564034487,0.00052277903519083193,0.0003855554857880858,0.00024935398936123238,0.00011388911344806828,1.7370932607258165e-05,0.00014472655932015152,0.00026488971969998746,0.00037842629678879901,0.00048239150573450835,0.00057762147799533163,0.00066155356137520863,0.00073536536567634682,0.00079690668062753947,0.00084765960137188866,0.00088583414224094792,0.00091325185580031832,0.00092847914379989534,0.00093356952524535771,0.00092740896094415043,0.00091227815427148663,0.00088728832313883282,0.00085488168180893791,0.00081437176238295401,0.00076826172775274783,0.00071598910580776413,0.00066009980794352668,0.00060006186208474087,0.00053840440699782989,0.00047458260340285847,0.0004110429707903051,0.00034718882631864226,0.00028533889325209626,0.00022479928438087689,0.00016771808883623627,0.00011329078700827217,6.3474980126822174e-05,1.7321099396079467e-05,2.3408809951995068e-05,5.9808057901980588e-05,9.0322446108292756e-05,0.00011619163775434552,0.00013606625998917511,0.00015130657563116806,0.00016081240871854613,0.00016614125856515095,0.00016638225590388667,0.00016320335041313636,0.00015595904846619018,0.00014643171227935267,0.0001343116191705268,0.00012156651676618424,0.0001085655362124675,9.7913906506694222e-05,9.3950714308797462e-05,9.6673011194299828e-05,9.7354655166689215e-05,9.7241752232316353e-05,9.4162910139826972e-05,9.2256696622401845e-05,9.0832833618707158e-05,9.1460369735924543e-05,9.2667594742948452e-05,9.5869689410633995e-05,9.9511629804611664e-05,0.00010497221045051503,0.00011071989608895786,0.00011805669390280862,0.00012545325059535966,0.00013413419728635335,0.00014244180627666551,0.00015164157395086215,0.00016000532769817492,0.00016767130170837791,0.00017351996368466596,0.00017941684939523934,0.00018412082302173279,0.00018913403030552242,0.00019316281813592709,0.00019763002995771547,0.00020123118458437744,0.00020534352760895525,0.00020864516533857953,0.0002124845309436522,0.00021552253480049637,0.00021908551176708858,0.00022184281989936184,0.00022510475346279197,0.00022753524174396985,0.00023042583280644531,0.00023243706398459233,0.00023486201551710227,0.00023635752134142492,0.00023821205198332762,0.00023909818816381399,0.00024030322298231971,0.00024050915589183047,]
mtf_1500um = [1,0.97427152376883641,0.93609645679290765,0.90020846747927752,0.86400731816292264,0.82860247931248454,0.79344654602505793,0.75887756740532819,0.72466103106942659,0.69099507198705312,0.65772230267507359,0.62500041383135196,0.59270538573234011,0.56097231757422783,0.52970530392109105,0.49901960463628403,0.4688427534370212,0.43927633845446123,0.41026269971021989,0.38189606851830171,0.35413035192311676,0.32705336896682358,0.30062763675210019,0.27493979211995212,0.24995531063878912,0.22576470977726201,0.20233560785159246,0.17976800237506058,0.15803122607546141,0.13723871394125814,0.11736504489055187,0.098547787711899218,0.080769566664723194,0.064210995409206884,0.048871536846598951,0.035015005923280954,0.022680960938349003,0.012351694819420375,0.0042439538729576202,0.00024100108130352266,2.6005459509089053e-05,3.4213418387141814e-06,2.5364408846386247e-05,1.3014902049660019e-06,1.8862766719690372e-05,1.0246124240145474e-06,1.4321783159203599e-05,7.0955800120397513e-07,1.1425627297908847e-05,7.5699782750679905e-07,9.6163664541487953e-06,1.1793029808158957e-06,8.8466689824188619e-06,2.1157957292944098e-06,8.9491368747613201e-06,3.5006810804225362e-06,9.6436745355977784e-06,5.1042494933811107e-06,1.0544497681590383e-05,6.4088535023800703e-06,8.9177952348928098e-06,4.2749267700789535e-06,1.8681465319775813e-05,4.2644130029129574e-05,9.5612940187530943e-05,0.00016593218924889933,0.00026826308557959834,0.00038905244742312598,0.00053890230170750215,0.00070279624789444282,0.00088828525639944285,0.001079637166637272,0.001282477273046141,0.001481218346110781,0.0016806470543566886,0.0018661054641187942,0.0020424616954500146,0.0021966341679616132,0.0023342328627490149,0.0024440050731673857,0.0025326589802768676,0.002591309308146837,0.0026278313473478117,0.0026350394362731296,0.002622192070708265,0.0025837355601469347,0.00252995258275545,0.002456422046216337,0.0023741331722302544,0.0022791601636914368,0.0021829287688644324,0.0020813562665796177,0.0019860188796631097,0.0018921579181025298,0.0018112797564104025,0.0017374186608291764,0.0016821928313073677,0.0016372723264938261,0.0016142732059417383,0.0015207532480173696,0.0013532547958019679,0.0011666312342605884,0.00095788321640577143,0.00073570736938776738,0.00050435544624591691,0.00027083494458976786,4.1808424612503446e-05,0.00017721454714922393,0.00037953613539008112,0.00056161420828231543,0.00071805898962803863,0.0008475630096619163,0.00094667774796018027,0.0010163870830704404,0.0010552353470926123,0.0010662882582342151,0.0010497912727962157,0.0010103987090512535,0.00094958129363871731,0.00087311860438534514,0.00078265059593665145,0.00068384498724662491,0.00057895422612608738,0.00047379676276546712,0.00037013220297011469,0.00027310538339542234,0.00018360297145690528,0.00010573953398977591,3.9286486075159123e-05,1.2849266668284861e-05,5.2107620508257299e-05,7.6825024066491608e-05,8.9631226522591777e-05,9.0064665794245511e-05,8.1898840244562642e-05,6.5969127613367862e-05,4.7481444378083811e-05,3.0753265322074866e-05,2.6420181577914164e-05,2.4788157938762831e-05,2.3225887082258288e-05,2.0883070113143681e-05,1.9077726068094852e-05,1.6530394936634519e-05,1.4715861048165098e-05,1.2269380377450638e-05,1.071371725597779e-05,8.6360731712854962e-06,7.5521820199562303e-06,6.0267009840062058e-06,5.5429418009281862e-06,4.6467555455600363e-06,4.7761597160092827e-06,4.4627551827580031e-06,5.0900052469037547e-06,5.1792451077638532e-06,6.0450152334688618e-06,6.1960374995798832e-06,6.4391420601093185e-06,4.5854299484492324e-06,3.4692973607994116e-06,2.8415495017711529e-06,4.7149328919663608e-06,8.1859253214062121e-06,1.4897852319641678e-05,2.3629479557852613e-05,3.5705300528234342e-05,4.9632979271577675e-05,6.6461100996641158e-05,8.4482903445438464e-05,0.00010453795444712777,0.00012478484726496602,0.00014594133187589915,0.00016612355664185168,0.00018602129797467797,0.00020380390444229833,0.00022022574120125234,0.00023354420756442059,0.00024460190063724214,0.00025228072833888884,0.000257440914926841,0.00025844731146043478,0.00025646898373124288,0.00025031302313122469,0.00024141401907224185,0.00022884303913552954,0.00021424877243758435,0.00019689229851829103,0.000178576527789494,0.00015868105939262353,0.00013907792635126488,0.0001191951362166496,0.0001008890161591134,8.354659301498292e-05,6.8969714309426858e-05,5.6333619524242593e-05,4.7603436465048502e-05,3.9180521428325404e-05,2.6537369838699484e-05,1.0759120467453804e-05,6.2958551653467457e-06,2.523445174357742e-05,4.4404733654809258e-05,6.4287149771746915e-05,8.316652939890317e-05,0.00010153338386757522,0.00011773995634435896,0.00013237888311392752,0.00014397105313371174,0.00015328283376471967,0.00015904938103876144,0.00016226185597414936,0.00016186846233447606,0.00015909186368589216,0.00015305833839688478,0.00014518777673009318,0.00013469663482408353,0.00012340140265541772,0.00011023919416818685,9.5227396284987615e-05,7.7852028641400435e-05,5.970387883459976e-05,4.0429152661381666e-05,2.1614932861923972e-05,2.8738130344862337e-06,1.4274731764942568e-05,3.0335184419970462e-05,4.3918252311120343e-05,5.5707720133050157e-05,6.4493243151135383e-05,7.1177644984205096e-05,7.4761016417356689e-05,7.6393289569947568e-05,7.5304574156206963e-05,7.2955892284741694e-05,6.8924772558253162e-05,6.5677397830484404e-05,6.211848551200498e-05,5.8178291032036169e-05,5.3215224208233791e-05,4.8237360842268621e-05,4.2530839319852973e-05,3.7149734703995328e-05,3.1364742703857738e-05,2.6244025280489641e-05,2.1028822764406934e-05,1.6765575313775718e-05,1.2648402725880269e-05,9.6758806973025133e-06,6.9772101746280077e-06,5.48350347810432e-06,4.247685526680349e-06,4.1210267789108183e-06,4.0730741452953211e-06,4.8609674624579649e-06,5.3468896574965507e-06,]

mtf_array_no_shift = np.column_stack([x,mtf_no_shift])
mtf_array_500um = np.column_stack([x,mtf_500um])
mtf_array_1500um = np.column_stack([x,mtf_1500um])
# mtf_array_no_shift.append(1)

plt.figure(dpi=300)
plt.plot(x, mtf_500um)
plt.title('MTF with +/-0.5mm source lateral shift')
plt.xlabel('Line Density X (cycles/mm)')
plt.ylabel('MTF (normalized)')
plt.grid()

plt.figure(dpi=300)
plt.plot(x, mtf_1500um)
plt.title('MTF with +/-1.5mm source lateral shift')
plt.xlabel('Line Density X (cycles/mm)')
plt.ylabel('MTF (normalized)')
plt.grid()

plt.figure(dpi=300)
plt.plot(x, mtf_no_shift)
plt.plot(x, mtf_500um)
plt.plot(x, mtf_1500um)
plt.title('MTF')
plt.xlabel('Line Density X (cycles/mm)')
plt.ylabel('MTF (normalized)')
plt.grid()
plt.legend(['No shift','+/-0.5mm shift','+/-1.5mm shift'])


# plt.figure(dpi=300)
# plt.plot(d65wavelength,d65flux)
# plt.title('D65 spectrum')
# plt.xlabel('Wavelength (nm)')
# plt.ylabel('Normalized Flux (Watts/nm)')
# plt.xlim((350,850))
# plt.xticks(np.linspace(350,850,11))
# plt.ylim(((0,1)))
# plt.grid()
# plt.savefig('q4_D65_Spectrum.png')
