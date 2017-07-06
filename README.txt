#################################################################################
# SAIKRISHNA KANUKUNTLA								#
# SXK160432									#		
# CS 6322.001 : Information Retrieval						#
# Fall 2016									#
# Homework # 3									#				
#################################################################################

Instructions to compile the code.

The main file to complie is HW3_IR.py 
all the other py files are supporting files.

something like this in the command prompt would run the code

$ python HW3_IR.py


I have included the cranfield collection locally and gave the local path and included
it in the code.

PS: THE CODE RUNS FOR AROUND 30 MINUTES TO GET CALCULATE THE COSINE SCORES AND GET THE 
    TOP 5 DOCS. 



#################################################################################
1.VECTOR REPRESENTATIONS OF THE QUERIES  :  

Weighting Scheme 1

Q1 = [['similarity', 0.22642823590310956], [u'law', 0.22642823590310956], ['must', 0.22642823590310956], [u'obey', 0.22642823590310956], [u'construct', 0.22642823590310956], ['aeroelastic', 0.22642823590310956], [u'model', 0.22642823590310956], ['heated', 0.22642823590310956], ['high', 0.22642823590310956], ['speed', 0.22642823590310956], ['aircraft', 0.22642823590310956]]
Q2 = [['realgas', 0.23747993729073966], ['transport', 0.23747993729073966], [u'property', 0.23747993729073966], ['air', 0.23747993729073966], ['available', 0.23747993729073966], ['over', 0.23747993729073966], ['wide', 0.23747993729073966], ['range', 0.23747993729073966], [u'enthalpy', 0.23747993729073966], [u'density', 0.23747993729073966]]
Q3 = [['possible', 0.21678853101508402], ['to', 0.21678853101508402], ['find', 0.21678853101508402], ['analytical', 0.21678853101508402], ['similar', 0.21678853101508402], ['solution', 0.21678853101508402], ['strong', 0.21678853101508402], ['blast', 0.21678853101508402], ['wave', 0.21678853101508402], ['problem', 0.21678853101508402], ['newtonian', 0.21678853101508402], ['approximation', 0.21678853101508402]]
Q4 = [['can', 0.2503258334775646], ['aerodynamic', 0.2503258334775646], ['performance', 0.2503258334775646], ['channel', 0.2503258334775646], ['flow', 0.2503258334775646], ['ground', 0.2503258334775646], ['effect', 0.2503258334775646], [u'machine', 0.2503258334775646], [u'calculate', 0.2503258334775646]]
Q5 = [['basic', 0.33584734810807615], ['mechanism', 0.33584734810807615], ['transonic', 0.33584734810807615], ['aileron', 0.33584734810807615], ['buzz', 0.33584734810807615]]
Q6 = [[u'paper', 0.37548875021634687], ['shocksound', 0.37548875021634687], ['wave', 0.37548875021634687], ['interaction', 0.37548875021634687]]
Q7 = [['material', 0.45021313014394093], [u'property', 0.31072107392856274], ['photoelastic', 0.31072107392856274], [u'material', 0.45021313014394093]]
Q8 = [['can', 0.22642823590310956], ['transverse', 0.22642823590310956], ['potential', 0.22642823590310956], ['flow', 0.22642823590310956], ['about', 0.22642823590310956], ['body', 0.22642823590310956], ['revolution', 0.22642823590310956], [u'calculate', 0.22642823590310956], ['efficiently', 0.22642823590310956], ['electronic', 0.22642823590310956], ['computer', 0.22642823590310956]]
Q9 = [['can', 0.17235704067948768], ['threedimensional', 0.17235704067948768], ['problem', 0.24973331163401866], ['transverse', 0.17235704067948768], ['potential', 0.17235704067948768], ['flow', 0.17235704067948768], ['about', 0.17235704067948768], ['body', 0.17235704067948768], ['revolution', 0.17235704067948768], [u'reduce', 0.17235704067948768], ['to', 0.17235704067948768], ['twodimensional', 0.17235704067948768], ['problem', 0.24973331163401866]]
Q10 =[['experimental', 0.2503258334775646], ['pressure', 0.2503258334775646], [u'distribution', 0.2503258334775646], [u'body', 0.2503258334775646], ['revolution', 0.2503258334775646], ['at', 0.2503258334775646], ['angle', 0.2503258334775646], ['attack', 0.2503258334775646], ['available', 0.2503258334775646]]
Q11 =[[u'do', 0.20070717941392996], ['exist', 0.20070717941392996], ['good', 0.20070717941392996], ['basic', 0.20070717941392996], ['treatment', 0.20070717941392996], [u'dynamic', 0.20070717941392996], ['reentry', 0.20070717941392996], [u'combine', 0.20070717941392996], ['consideration', 0.20070717941392996], ['realistic', 0.20070717941392996], [u'effect', 0.20070717941392996], ['relative', 0.20070717941392996], ['simplicity', 0.20070717941392996], [u'result', 0.20070717941392996]]
Q12 =[['structural', 0.2655106415372406], ['aeroelastic', 0.2655106415372406], [u'problem', 0.2655106415372406], [u'associate', 0.2655106415372406], ['flight', 0.2655106415372406], ['high', 0.2655106415372406], ['speed', 0.2655106415372406], ['aircraft', 0.2655106415372406]]
Q13 =[[u'have', 0.18213879745566638], ['anyone', 0.18213879745566638], ['formally', 0.18213879745566638], [u'determine', 0.18213879745566638], ['influence', 0.18213879745566638], ['joule', 0.18213879745566638], ['heating', 0.18213879745566638], [u'produce', 0.18213879745566638], ['induced', 0.18213879745566638], ['current', 0.18213879745566638], ['magnetohydrodynamic', 0.18213879745566638], ['free', 0.18213879745566638], ['convection', 0.18213879745566638], [u'flow', 0.18213879745566638], ['under', 0.18213879745566638], ['general', 0.18213879745566638], [u'condition', 0.18213879745566638]]
Q14 =[[u'problem', 0.2655106415372406], ['heat', 0.2655106415372406], ['conduction', 0.2655106415372406], ['composite', 0.2655106415372406], [u'slab', 0.2655106415372406], [u'solve', 0.2655106415372406], ['so', 0.2655106415372406], ['far', 0.2655106415372406]]
Q15=[['can', 0.16792367405403807], ['criterion', 0.16792367405403807], [u'develop', 0.16792367405403807], ['to', 0.16792367405403807], ['show', 0.16792367405403807], ['empirically', 0.16792367405403807], ['validity', 0.16792367405403807], ['flow', 0.16792367405403807], [u'solution', 0.16792367405403807], ['chemically', 0.16792367405403807], [u'react', 0.16792367405403807], ['gas', 0.16792367405403807], [u'mixture', 0.16792367405403807], [u'base', 0.16792367405403807], [u'simplify', 0.16792367405403807], ['assumption', 0.16792367405403807], ['instantaneous', 0.16792367405403807], ['local', 0.16792367405403807], ['chemical', 0.16792367405403807], ['equilibrium', 0.16792367405403807]]
Q16=[['chemical', 0.2655106415372406], ['kinetic', 0.2655106415372406], ['system', 0.2655106415372406], ['applicable', 0.2655106415372406], ['to', 0.2655106415372406], ['hypersonic', 0.2655106415372406], ['aerodynamic', 0.2655106415372406], [u'problem', 0.2655106415372406]]
Q17=[['theoretical', 0.23747993729073966], ['experimental', 0.23747993729073966], [u'guide', 0.23747993729073966], ['do', 0.23747993729073966], ['we', 0.23747993729073966], ['to', 0.23747993729073966], ['turbulent', 0.23747993729073966], ['couette', 0.23747993729073966], ['flow', 0.23747993729073966], ['behaviour', 0.23747993729073966]]
Q18=[['possible', 0.13249191109670833], ['to', 0.19197152371877974], ['relate', 0.13249191109670833], ['available', 0.13249191109670833], ['pressure', 0.19197152371877974], [u'distribution', 0.13249191109670833], ['ogive', 0.19197152371877974], ['forebody', 0.19197152371877974], ['at', 0.19197152371877974], ['zero', 0.13249191109670833], ['angle', 0.19197152371877974], ['attack', 0.19197152371877974], ['to', 0.19197152371877974], [u'low', 0.13249191109670833], ['surface', 0.13249191109670833], [u'pressure', 0.19197152371877974], ['equivalent', 0.13249191109670833], ['ogive', 0.19197152371877974], ['forebody', 0.19197152371877974], ['at', 0.19197152371877974], ['angle', 0.19197152371877974], ['attack', 0.19197152371877974]]
Q19=[['methods', 0.17235704067948768], ['dash', 0.24973331163401866], ['exact', 0.17235704067948768], ['approximate', 0.17235704067948768], ['dash', 0.24973331163401866], ['presently', 0.17235704067948768], ['available', 0.17235704067948768], [u'predict', 0.17235704067948768], ['body', 0.17235704067948768], [u'pressure', 0.17235704067948768], ['at', 0.17235704067948768], ['angle', 0.17235704067948768], ['attack', 0.17235704067948768]]
Q20=[[u'paper', 0.2838428151928298], ['internal', 0.2838428151928298], ['slip', 0.2838428151928298], ['flow', 0.2838428151928298], ['heat', 0.2838428151928298], ['transfer', 0.2838428151928298], [u'study', 0.2838428151928298]]


Weighting Scheme 2

Q1[['similarity', 0.22967298943488776], [u'law', 0.22967298943488776], ['must', 0.22967298943488776], [u'obey', 0.22967298943488776], [u'construct', 0.22967298943488776], ['aeroelastic', 0.22967298943488776], [u'model', 0.22967298943488776], ['heated', 0.22967298943488776], ['high', 0.22967298943488776], ['speed', 0.22967298943488776], ['aircraft', 0.22967298943488776]]
Q2[['realgas', 0.24188650172516024], ['transport', 0.24188650172516024], [u'property', 0.24188650172516024], ['air', 0.24188650172516024], ['available', 0.24188650172516024], ['over', 0.24188650172516024], ['wide', 0.24188650172516024], ['range', 0.24188650172516024], [u'enthalpy', 0.24188650172516024], [u'density', 0.24188650172516024]]
Q3[['possible', 0.21899492969261666], ['to', 0.21899492969261666], ['find', 0.21899492969261666], ['analytical', 0.21899492969261666], ['similar', 0.21899492969261666], ['solution', 0.21899492969261666], ['strong', 0.21899492969261666], ['blast', 0.21899492969261666], ['wave', 0.21899492969261666], ['problem', 0.21899492969261666], ['newtonian', 0.21899492969261666], ['approximation', 0.21899492969261666]]
Q4[['can', 0.256047197640118], ['aerodynamic', 0.256047197640118], ['performance', 0.256047197640118], ['channel', 0.256047197640118], ['flow', 0.256047197640118], ['ground', 0.256047197640118], ['effect', 0.256047197640118], [u'machine', 0.256047197640118], [u'calculate', 0.256047197640118]]
Q5[['basic', 0.34956512235409554], ['mechanism', 0.34956512235409554], ['transonic', 0.34956512235409554], ['aileron', 0.34956512235409554], ['buzz', 0.34956512235409554]]
Q6[[u'paper', 0.3925925925925926], ['shocksound', 0.3925925925925926], ['wave', 0.3925925925925926], ['interaction', 0.3925925925925926]]
Q7[['material', 0.4345864661654135], [u'property', 0.3925925925925926], ['photoelastic', 0.3925925925925926], [u'material', 0.4345864661654135]]
Q8[['can', 0.22967298943488776], ['transverse', 0.22967298943488776], ['potential', 0.22967298943488776], ['flow', 0.22967298943488776], ['about', 0.22967298943488776], ['body', 0.22967298943488776], ['revolution', 0.22967298943488776], [u'calculate', 0.22967298943488776], ['efficiently', 0.22967298943488776], ['electronic', 0.22967298943488776], ['computer', 0.22967298943488776]]
Q9[['can', 0.20955340746286433], ['threedimensional', 0.20955340746286433], ['problem', 0.2347800830534691], ['transverse', 0.20955340746286433], ['potential', 0.20955340746286433], ['flow', 0.20955340746286433], ['about', 0.20955340746286433], ['body', 0.20955340746286433], ['revolution', 0.20955340746286433], [u'reduce', 0.20955340746286433], ['to', 0.20955340746286433], ['twodimensional', 0.20955340746286433], ['problem', 0.2347800830534691]]
Q10[['experimental', 0.256047197640118], ['pressure', 0.256047197640118], [u'distribution', 0.256047197640118], [u'body', 0.256047197640118], ['revolution', 0.256047197640118], ['at', 0.256047197640118], ['angle', 0.256047197640118], ['attack', 0.256047197640118], ['available', 0.256047197640118]]
Q11[[u'do', 0.20112540916799396], ['exist', 0.20112540916799396], ['good', 0.20112540916799396], ['basic', 0.20112540916799396], ['treatment', 0.20112540916799396], [u'dynamic', 0.20112540916799396], ['reentry', 0.20112540916799396], [u'combine', 0.20112540916799396], ['consideration', 0.20112540916799396], ['realistic', 0.20112540916799396], [u'effect', 0.20112540916799396], ['relative', 0.20112540916799396], ['simplicity', 0.20112540916799396], [u'result', 0.20112540916799396]]
Q12[['structural', 0.2727411870290969], ['aeroelastic', 0.2727411870290969], [u'problem', 0.2727411870290969], [u'associate', 0.2727411870290969], ['flight', 0.2727411870290969], ['high', 0.2727411870290969], ['speed', 0.2727411870290969], ['aircraft', 0.2727411870290969]]
Q13[[u'have', 0.18039839878735509], ['anyone', 0.18039839878735509], ['formally', 0.18039839878735509], [u'determine', 0.18039839878735509], ['influence', 0.18039839878735509], ['joule', 0.18039839878735509], ['heating', 0.18039839878735509], [u'produce', 0.18039839878735509], ['induced', 0.18039839878735509], ['current', 0.18039839878735509], ['magnetohydrodynamic', 0.18039839878735509], ['free', 0.18039839878735509], ['convection', 0.18039839878735509], [u'flow', 0.18039839878735509], ['under', 0.18039839878735509], ['general', 0.18039839878735509], [u'condition', 0.18039839878735509]]
Q14[[u'problem', 0.2727411870290969], ['heat', 0.2727411870290969], ['conduction', 0.2727411870290969], ['composite', 0.2727411870290969], [u'slab', 0.2727411870290969], [u'solve', 0.2727411870290969], ['so', 0.2727411870290969], ['far', 0.2727411870290969]]
Q15[['can', 0.1644591931838555], ['criterion', 0.1644591931838555], [u'develop', 0.1644591931838555], ['to', 0.1644591931838555], ['show', 0.1644591931838555], ['empirically', 0.1644591931838555], ['validity', 0.1644591931838555], ['flow', 0.1644591931838555], [u'solution', 0.1644591931838555], ['chemically', 0.1644591931838555], [u'react', 0.1644591931838555], ['gas', 0.1644591931838555], [u'mixture', 0.1644591931838555], [u'base', 0.1644591931838555], [u'simplify', 0.1644591931838555], ['assumption', 0.1644591931838555], ['instantaneous', 0.1644591931838555], ['local', 0.1644591931838555], ['chemical', 0.1644591931838555], ['equilibrium', 0.1644591931838555]]
Q16[['chemical', 0.2727411870290969], ['kinetic', 0.2727411870290969], ['system', 0.2727411870290969], ['applicable', 0.2727411870290969], ['to', 0.2727411870290969], ['hypersonic', 0.2727411870290969], ['aerodynamic', 0.2727411870290969], [u'problem', 0.2727411870290969]]
Q17[['theoretical', 0.24188650172516024], ['experimental', 0.24188650172516024], [u'guide', 0.24188650172516024], ['do', 0.24188650172516024], ['we', 0.24188650172516024], ['to', 0.24188650172516024], ['turbulent', 0.24188650172516024], ['couette', 0.24188650172516024], ['flow', 0.24188650172516024], ['behaviour', 0.24188650172516024]]
Q18[['possible', 0.15567036432314413], ['to', 0.17609069405480451], ['relate', 0.15567036432314413], ['available', 0.15567036432314413], ['pressure', 0.17609069405480451], [u'distribution', 0.15567036432314413], ['ogive', 0.17609069405480451], ['forebody', 0.17609069405480451], ['at', 0.17609069405480451], ['zero', 0.15567036432314413], ['angle', 0.17609069405480451], ['attack', 0.17609069405480451], ['to', 0.17609069405480451], [u'low', 0.15567036432314413], ['surface', 0.15567036432314413], [u'pressure', 0.17609069405480451], ['equivalent', 0.15567036432314413], ['ogive', 0.17609069405480451], ['forebody', 0.17609069405480451], ['at', 0.17609069405480451], ['angle', 0.17609069405480451], ['attack', 0.17609069405480451]]
Q19[['methods', 0.20955340746286433], ['dash', 0.2347800830534691], ['exact', 0.20955340746286433], ['approximate', 0.20955340746286433], ['dash', 0.2347800830534691], ['presently', 0.20955340746286433], ['available', 0.20955340746286433], [u'predict', 0.20955340746286433], ['body', 0.20955340746286433], [u'pressure', 0.20955340746286433], ['at', 0.20955340746286433], ['angle', 0.20955340746286433], ['attack', 0.20955340746286433]]
Q20[[u'paper', 0.2928373394485904], ['internal', 0.2928373394485904], ['slip', 0.2928373394485904], ['flow', 0.2928373394485904], ['heat', 0.2928373394485904], ['transfer', 0.2928373394485904], [u'study', 0.2928373394485904]]




2.
TOP 5 DOCUMENTS RETURNED BY THE RETREIVAL SYSTEM FOR THE WEIGHTING SCHEME 1

1 ################################################################################
  [[883, 0.012515546320487472], [1041, 0.009871526533440842], [1167, 0.00920057772563204], [252, 0.008797308796326396], [1164, 0.008711899840094638]]
  ['similarity', u'law', 'must', u'obey', u'construct', 'aeroelastic', u'model', 'heated', 'high', 'speed', 'aircraft']
1 0.0125155463205 883 
the estimation of fatigue damage on structural elements 
2 0.00987152653344 1041 
on transverse vibrations of thin shallow elastic shells 
3 0.00920057772563 1167 
damage incurred on a tiltwing multipropeller vtolstol
aircraft operating over a level gravelcovered surface 
4 0.00879730879633 252 
on the ground level disturbance from large aircraft
flying at supersonic speeds 
5 0.00871189984009 1164 
an investigation of the effect of downwash from a vtol
aircraft and a helicopter in the ground environment 


2 ##################################################################################################
 [[1102, 0.011141833214031959], [1149, 0.01108974957014422], [620, 0.010363651632741324], [615, 0.00991143441500507], [618, 0.009417916488787533]]
 ['realgas', 'transport', u'property', 'air', 'available', 'over', 'wide', 'range', u'enthalpy', u'density']

1 0.011141833214 1102 
pressures densities and temperatures in the upper atmosphere 
2 0.0110897495701 1149 
preliminary results of density measurements from an air force satellite
3 0.0103636516327 620 
latitude and diurnal variations of air densities from  to  km
as derived from the orbits of discoverer satellites 
4 0.00991143441501 615 
determination of upperatmosphere air density and scale height from
satellite observations 
5 0.00941791648879 618 
density of the upper atmosphere from analysis of satellite orbits 
further results 

3 ##################
 [[1151, 0.009584453054715045], [506, 0.009458003912610351], [1015, 0.007825673149237137], [280, 0.0077224278570474075], [919, 0.007049579893351908]]
 ['possible', 'to', 'find', 'analytical', 'similar', 'solution', 'strong', 'blast', 'wave', 'problem', 'newtonian', 'approximation']
1 0.00958445305472 1151 
on periodically oscillating wakes in the oseen approximation 
2 0.00945800391261 506 
energy equation approximations in fluid mechanics 
3 0.00782567314924 1015 
principles of creep buckling weightstrength analysis
4 0.00772242785705 280 
higher order approximations for relaxation oscillations 
5 0.00704957989335 919 
supersonic flow over an inclined wing of zero aspect ratio 

4 ##################
  [[202, 0.00923647841282729], [631, 0.008044378703400253], [675, 0.0073939507048134505], [338, 0.007222072586593633], [1305, 0.007222072586593633]]
  ['can', 'aerodynamic', 'performance', 'channel', 'flow', 'ground', 'effect', u'machine', u'calculate']
1 0.00923647841283 202 
calculated velocity distributions and force derivatives
for a series of highspeed aerofoils 
2 0.0080443787034 631 
calculated lift distributions in incompressible flow
on some sweptback wings 
3 0.00739395070481 675 
a simple method for calculating the span and chordwise loading on
straight and swept wings of any aspect ratio at subsonic speeds 
4 0.00722207258659 338 
experimental evaluation of heat transfer with transpiration
cooling in a turbulent boundary layer at m 
5 0.00722207258659 1305 
experiments on circular cones at yaw in supersonic
flow 

5 ##################
 [[495, 0.031099585804484246], [0, 0.0], [1, 0.0], [2, 0.0], [3, 0.0]]
 ['basic', 'mechanism', 'transonic', 'aileron', 'buzz']
1 0.0310995858045 495 
a theory of transonic aileron buzz neglecting viscous
effects 
2 0.0 0 
experimental investigation of the aerodynamics of a
wing in a slipstream 
3 0.0 1 
simple shear flow past a flat plate in an incompressible fluid of small
viscosity 
4 0.0 2 
the boundary layer in simple shear flow past a flat plate 
5 0.0 3 
approximate solutions of the incompressible laminar
boundary layer equations for a plate in shear flow 

6 ##################
 [[290, 0.019964746412908577], [968, 0.01851799897869547], [972, 0.01653781248253761], [1287, 0.0160596353570962], [325, 0.015233210332641528]]
 [u'paper', 'shocksound', 'wave', 'interaction']
1 0.0199647464129 290 
sweepback effects in the turbulent boundarylayer shockwave
interaction 
2 0.0185179989787 968 
on the use of sidejets as control devices 
3 0.0165378124825 972 
interaction effects produced by jet exhausting laterally near base of
ogivecylinder model in supersonic main stream 
4 0.0160596353571 1287 
analysis of the fluid mechanics of secondary injection
for thrust vector control 
5 0.0152332103326 325 
forstorder slip effects on the compressible laminar
boundary layer over a slender body of revolution in
axial flow 

7 ##################
 [[760, 0.02446194897377737], [1095, 0.02212666537822878], [1098, 0.02021203567850563], [1116, 0.01884374591507025], [865, 0.018729634147067423]]
 ['material', u'property', 'photoelastic', u'material']
1 0.0244619489738 760 
buckling of sandwich under normal pressure 
2 0.0221266653782 1095 
qualitative measurements of the effective heats of
ablation of several materials in supersonic air jets
at stagnation temperature up to  f
3 0.0202120356785 1098 
a theoretical study of stagnation point ablation 
4 0.0188437459151 1116 
stability of orthotropic cylindrical shells under combined
loading 
5 0.0187296341471 865 
regularities in creep and hot fatigue data 

8 ##################
 [[744, 0.015522048442082477], [110, 0.013121296870517602], [1062, 0.011888997145869924], [944, 0.01168970176825349], [1005, 0.01015818496397777]]
 ['can', 'transverse', 'potential', 'flow', 'about', 'body', 'revolution', u'calculate', 'efficiently', 'electronic', 'computer']
1 0.0155220484421 744 
an automatic method for finding the greatest or least
value function 
2 0.0131212968705 110 
the laminar boundary layer equation a method of solution
by means of an automatic computer 
3 0.0118889971459 1062 
on obtaining solutions to the navierstokes equations
with high speed digital computers 
4 0.0116897017683 944 
method for design of pump impellers using a high speed
digital computer 
5 0.010158184964 1005 
freeflight measurements of the static and dynamic

9 ##################
 [[319, 0.009104725931384089], [606, 0.00831143962086883], [180, 0.007384907897976163], [853, 0.007175243420535543], [532, 0.007050447058533388]]
 ['can', 'threedimensional', 'problem', 'transverse', 'potential', 'flow', 'about', 'body', 'revolution', u'reduce', 'to', 'twodimensional', 'problem']
1 0.00910472593138 319 
comment on improved numerical solution of the blasius problem with
threepoint boundary conditions 
2 0.00831143962087 606 
duct flow in magnetohydrodynamics 
3 0.00738490789798 180 
some problems on heat conduction in stratiform bodies 
4 0.00717524342054 853 
boundaryvalue problems of the thinwalled circular
cylinder 
5 0.00705044705853 532 
stagnationpoint shockdetachment distance for flow
around spheres and cylinders in air 

10 ##################
 [[290, 0.009265909775931792], [905, 0.00923333814039018], [727, 0.009162376808244036], [253, 0.008782656423941165], [608, 0.008523397317126511]]
 ['experimental', 'pressure', u'distribution', u'body', 'revolution', 'at', 'angle', 'attack', 'available']
1 0.00926590977593 290 
sweepback effects in the turbulent boundarylayer shockwave
interaction 
2 0.00923333814039 905 
review of the pitot tube 
3 0.00916237680824 727 
free vibrations of continuous skin stringer panels 
4 0.00878265642394 253 
boundary layers with suction and injection  a review
of published work on skin friction 
5 0.00852339731713 608 
on three dimensional bodies of delta planform which
can support plane attached shock waves 

11 ##################
[[618, 0.002940332328689092], [1175, 0.0028799686442782376], [1089, 0.002827352081316574], [879, 0.00264386507734697], [934, 0.00264386507734697]]
11 [u'do', 'exist', 'good', 'basic', 'treatment', u'dynamic', 'reentry', u'combine', 'consideration', 'realistic', u'effect', 'relative', 'simplicity', u'result']
1 0.00294033232869 618 
density of the upper atmosphere from analysis of satellite orbits 
further results 
2 0.00287996864428 1175 
bending tests of ringstiffened circular cylinders 
3 0.00282735208132 1089 
pressure distribution and force measurements on a vtol
tilting wingpropeller model  pt ii analysis of
results 
4 0.00264386507735 879 
the design and testing of supersonic flutter models 
5 0.00264386507735 934 
buckling of thin single and multilayer conical and cylindrical
shells with rotationally symmetric stresses 

12 ##################
 [[883, 0.014675778926103642], [1041, 0.011575390906491519], [1167, 0.01078863369094623], [252, 0.010315758955580652], [1164, 0.010215608076995775]]
 ['structural', 'aeroelastic', u'problem', u'associate', 'flight', 'high', 'speed', 'aircraft']
1 0.0146757789261 883 
the estimation of fatigue damage on structural elements 

2 0.0115753909065 1041 
on transverse vibrations of thin shallow elastic shells 

3 0.0107886336909 1167 
damage incurred on a tiltwing multipropeller vtolstol
aircraft operating over a level gravelcovered surface 

4 0.0103157589556 252 
on the ground level disturbance from large aircraft
flying at supersonic speeds 

5 0.010215608077 1164 
an investigation of the effect of downwash from a vtol
aircraft and a helicopter in the ground environment 

13 ##################
   [[106, 0.004625794025070907], [319, 0.004478303219396933], [285, 0.004231598790737219], [477, 0.0038568115759456366], [297, 0.003731919349497445]]
    [u'have', 'anyone', 'formally', u'determine', 'influence', 'joule', 'heating', u'produce', 'induced', 'current', 'magnetohydrodynamic', 'free', 'convection', u'flow', 'under', 'general', u'condition']
1 0.00462579402507 106 
on the mixing of two parallel streams 

2 0.0044783032194 319 
comment on improved numerical solution of the blasius problem with
threepoint boundary conditions 

3 0.00423159879074 285 
effect of roll on dynamic instability of symmetric
missiles 

4 0.00385681157595 477 
tabulation of the blasius function with blowing and
suction 

5 0.0037319193495 297 
incompressible wedge flows of an electrically conducting
viscous fluid in the presence of a magnetic field 

14 ##################
  [[1140, 0.009833851457553706], [802, 0.008486231177910145], [653, 0.00834988746264576], [315, 0.00828335343449571], [272, 0.007695113624454735]]
  [u'problem', 'heat', 'conduction', 'composite', u'slab', u'solve', 'so', 'far']
1 0.00983385145755 1140 
the wake behind an oscillating vehicle 

2 0.00848623117791 802 
the shock pattern of a wingbody combination far from
the flight path 

3 0.00834988746265 653 
on the propagation and structure of the blast wave 
 part 

4 0.0082833534345 315 
the occurrence and development of boundary layer separations at high
incidences and high speeds 

5 0.00769511362445 272 
flow past slender blunt bodies  a review and extension 

15 ##################
   [[1311, 0.007058651715944578], [302, 0.006545656756179044], [1188, 0.00643722212356808], [1285, 0.006276171623141186], [1010, 0.0062211324852657545]]
   ['can', 'criterion', u'develop', 'to', 'show', 'empirically', 'validity', 'flow', u'solution', 'chemically', u'react', 'gas', u'mixture', u'base', u'simplify', 'assumption', 'instantaneous', 'local', 'chemical', 'equilibrium']
1 0.00705865171594 1311 
tabulated solutions of the equilibrium gas properties
behind the incidents and reflected normal shockwave
in a shocktube 

2 0.00654565675618 302 
effect of variable heat recombination on stagnation
point heat transfer 

3 0.00643722212357 1188 
nonequilibrium flow past a wedge 

4 0.00627617162314 1285 
equilibrium realgas performance charts for a shypersonic
shocktube windtunnel employing nitrogen 

5 0.00622113248527 1010 
freeflight measurements of the static and dynamic

16 ##################
   [[319, 0.009679932593875238], [606, 0.008836529061324936], [180, 0.007851462109142147], [853, 0.007628551719060065], [532, 0.007495871133038507]]
   ['chemical', 'kinetic', 'system', 'applicable', 'to', 'hypersonic', 'aerodynamic', u'problem']
1 0.00967993259388 319 
comment on improved numerical solution of the blasius problem with
threepoint boundary conditions 

2 0.00883652906132 606 
duct flow in magnetohydrodynamics 

3 0.00785146210914 180 
some problems on heat conduction in stratiform bodies 

4 0.00762855171906 853 
boundaryvalue problems of the thinwalled circular
cylinder 

5 0.00749587113304 532 
stagnationpoint shockdetachment distance for flow
around spheres and cylinders in air 

17 ##################
   [[882, 0.01295862946794374], [864, 0.011527589606207655], [264, 0.009866301195667383], [129, 0.009710769331629393], [740, 0.009460104905616563]]
   ['theoretical', 'experimental', u'guide', 'do', 'we', 'to', 'turbulent', 'couette', 'flow', 'behaviour']
1 0.0129586294679 882 
correlated fatigue data for aircraft structural joints 

2 0.0115275896062 864 
a study of the thermal fatigue behaviour of metals 
 the effect of test conditions on nickelbase high
temperature alloys 

3 0.00986630119567 264 
some instabilities arising from the interaction between
shock waves and boundary layer 

4 0.00971076933163 129 
the behaviour of nonlinear systems 

5 0.00946010490562 740 
the behaviour of thin cylindrical shells after buckling
under axial compression 

18 ##################
   [[491, 0.009352196354836926], [707, 0.007007751952093751], [353, 0.006841937052493597], [1349, 0.006322955813635726], [1114, 0.00626322613572205]]
   ['possible', 'to', 'relate', 'available', 'pressure', u'distribution', 'ogive', 'forebody', 'at', 'zero', 'angle', 'attack', 'to', u'low', 'surface', u'pressure', 'equivalent', 'ogive', 'forebody', 'at', 'angle', 'attack']
1 0.00935219635484 491 
prediction of ogiveforebody pressures at angles of attack 

2 0.00700775195209 707 
aerodynamic characteristics of two winged reentry vehicles at supersonic
 and hypersonic speeds 

3 0.00684193705249 353 
laminar heattransfer and pressure measurements over bluntnosed
cones at large angle of attack 

4 0.00632295581364 1349 
effects of jet billowing on stability of missiletype
bodies at mach   

5 0.00626322613572 1114 
measurements of aerodynamic forces for various mean
angles of attack on an airfoil oscillating in pitch
and on two finitespan wings oscillating in bending
with emphasis on damping in the stall 

19 ##################
[[491, 0.008396645795938419], [707, 0.006291742467222103], [353, 0.006142869525850262], [1349, 0.005676914634390669], [1114, 0.005623287771788791]]
19 ['methods', 'dash', 'exact', 'approximate', 'dash', 'presently', 'available', u'predict', 'body', u'pressure', 'at', 'angle', 'attack']
1 0.00839664579594 491 
prediction of ogiveforebody pressures at angles of attack 

2 0.00629174246722 707 
aerodynamic characteristics of two winged reentry vehicles at supersonic
 and hypersonic speeds 

3 0.00614286952585 353 
laminar heattransfer and pressure measurements over bluntnosed
cones at large angle of attack 

4 0.00567691463439 1349 
effects of jet billowing on stability of missiletype
bodies at mach   

5 0.00562328777179 1114 
measurements of aerodynamic forces for various mean
angles of attack on an airfoil oscillating in pitch
and on two finitespan wings oscillating in bending
with emphasis on damping in the stall 

20 ##################
   [[1151, 0.011591531201298348], [506, 0.009670644522421334], [548, 0.009140478594604578], [1268, 0.007839949256980438], [861, 0.007015822924273156]]
   [u'paper', 'internal', 'slip', 'flow', 'heat', 'transfer', u'study']
1 0.0115915312013 1151 
on periodically oscillating wakes in the oseen approximation 

2 0.00967064452242 506 
energy equation approximations in fluid mechanics 

3 0.0091404785946 548 
experimental study of the velocity and temperature
distribution in a highvelocity vortextype flow 

4 0.00783994925698 1268 
a study of supersonic combustion 

5 0.00701582292427 861 
the phenomenon of change in buckle pattern in elastic
structures 




[['similarity', 0.22967298943488776], [u'law', 0.22967298943488776], ['must', 0.22967298943488776], [u'obey', 0.22967298943488776], [u'construct', 0.22967298943488776], ['aeroelastic', 0.22967298943488776], [u'model', 0.22967298943488776], ['heated', 0.22967298943488776], ['high', 0.22967298943488776], ['speed', 0.22967298943488776], ['aircraft', 0.22967298943488776]]
[[883, 0.012515546320487472], [1041, 0.009871526533440842], [1167, 0.00920057772563204], [252, 0.008797308796326396], [1164, 0.008711899840094638], [1168, 0.008547097035655838], [881, 0.008365219649403274], [414, 0.008161456147550684], [11, 0.008060067663091777], [908, 0.007900656055595666]]
[['realgas', 0.24188650172516024], ['transport', 0.24188650172516024], [u'property', 0.24188650172516024], ['air', 0.24188650172516024], ['available', 0.24188650172516024], ['over', 0.24188650172516024], ['wide', 0.24188650172516024], ['range', 0.24188650172516024], [u'enthalpy', 0.24188650172516024], [u'density', 0.24188650172516024]]
[[1102, 0.011141833214031959], [1149, 0.01108974957014422], [620, 0.010363651632741324], [615, 0.00991143441500507], [618, 0.009417916488787533], [9, 0.008838567944905925], [1256, 0.00831034150027579], [474, 0.008280625698360562], [1394, 0.007828260851336814], [948, 0.007604543138724927]]
[['possible', 0.21899492969261666], ['to', 0.21899492969261666], ['find', 0.21899492969261666], ['analytical', 0.21899492969261666], ['similar', 0.21899492969261666], ['solution', 0.21899492969261666], ['strong', 0.21899492969261666], ['blast', 0.21899492969261666], ['wave', 0.21899492969261666], ['problem', 0.21899492969261666], ['newtonian', 0.21899492969261666], ['approximation', 0.21899492969261666]]
[[1151, 0.009584453054715045], [506, 0.009458003912610351], [1015, 0.007825673149237137], [280, 0.0077224278570474075], [919, 0.007049579893351908], [653, 0.006885674342614165], [472, 0.006764140607916216], [360, 0.006042497051444494], [776, 0.006023000658644682], [841, 0.005973328412314938]]
[['can', 0.256047197640118], ['aerodynamic', 0.256047197640118], ['performance', 0.256047197640118], ['channel', 0.256047197640118], ['flow', 0.256047197640118], ['ground', 0.256047197640118], ['effect', 0.256047197640118], [u'machine', 0.256047197640118], [u'calculate', 0.256047197640118]]
[[202, 0.00923647841282729], [631, 0.008044378703400253], [675, 0.0073939507048134505], [338, 0.007222072586593633], [1305, 0.007222072586593633], [323, 0.007200958647605378], [1331, 0.006733613546053219], [1010, 0.006599439414559388], [1333, 0.006519793280915198], [509, 0.006432337876473682]]
[['basic', 0.34956512235409554], ['mechanism', 0.34956512235409554], ['transonic', 0.34956512235409554], ['aileron', 0.34956512235409554], ['buzz', 0.34956512235409554]]
[[495, 0.031099585804484246], [0, 0.0], [1, 0.0], [2, 0.0], [3, 0.0], [4, 0.0], [5, 0.0], [6, 0.0], [7, 0.0], [8, 0.0]]
[[u'paper', 0.3925925925925926], ['shocksound', 0.3925925925925926], ['wave', 0.3925925925925926], ['interaction', 0.3925925925925926]]
[[290, 0.019964746412908577], [968, 0.01851799897869547], [972, 0.01653781248253761], [1287, 0.0160596353570962], [325, 0.015233210332641528], [344, 0.014894236262040391], [569, 0.014760472188459245], [408, 0.014644701991705679], [1298, 0.013938256783822165], [25, 0.01338285667319126]]
[['material', 0.4345864661654135], [u'property', 0.3925925925925926], ['photoelastic', 0.3925925925925926], [u'material', 0.4345864661654135]]
[[760, 0.02446194897377737], [1095, 0.02212666537822878], [1098, 0.02021203567850563], [1116, 0.01884374591507025], [865, 0.018729634147067423], [552, 0.017242496167237716], [462, 0.01715748547290059], [118, 0.016767084513932683], [1278, 0.016459472349395956], [461, 0.016389830242263353]]
[['can', 0.22967298943488776], ['transverse', 0.22967298943488776], ['potential', 0.22967298943488776], ['flow', 0.22967298943488776], ['about', 0.22967298943488776], ['body', 0.22967298943488776], ['revolution', 0.22967298943488776], [u'calculate', 0.22967298943488776], ['efficiently', 0.22967298943488776], ['electronic', 0.22967298943488776], ['computer', 0.22967298943488776]]
[[744, 0.015522048442082477], [110, 0.013121296870517602], [1062, 0.011888997145869924], [944, 0.01168970176825349], [1005, 0.01015818496397777], [424, 0.010006082115573831], [92, 0.00963690041383357], [91, 0.008963050860799852], [647, 0.008779166486023606], [1086, 0.008656115682231008]]
[['can', 0.20955340746286433], ['threedimensional', 0.20955340746286433], ['problem', 0.2347800830534691], ['transverse', 0.20955340746286433], ['potential', 0.20955340746286433], ['flow', 0.20955340746286433], ['about', 0.20955340746286433], ['body', 0.20955340746286433], ['revolution', 0.20955340746286433], [u'reduce', 0.20955340746286433], ['to', 0.20955340746286433], ['twodimensional', 0.20955340746286433], ['problem', 0.2347800830534691]]
[[319, 0.009104725931384089], [606, 0.00831143962086883], [180, 0.007384907897976163], [853, 0.007175243420535543], [532, 0.007050447058533388], [577, 0.0067862620330266365], [854, 0.006712093007887439], [1137, 0.006712093007887439], [550, 0.006620890550064341], [1028, 0.006533192763454896]]
[['experimental', 0.256047197640118], ['pressure', 0.256047197640118], [u'distribution', 0.256047197640118], [u'body', 0.256047197640118], ['revolution', 0.256047197640118], ['at', 0.256047197640118], ['angle', 0.256047197640118], ['attack', 0.256047197640118], ['available', 0.256047197640118]]
[[290, 0.009265909775931792], [905, 0.00923333814039018], [727, 0.009162376808244036], [253, 0.008782656423941165], [608, 0.008523397317126511], [1173, 0.007951347153860634], [18, 0.007745574916090729], [1213, 0.007734455653610892], [402, 0.0075655836512331], [1170, 0.007559411242561712]]
[[u'do', 0.20112540916799396], ['exist', 0.20112540916799396], ['good', 0.20112540916799396], ['basic', 0.20112540916799396], ['treatment', 0.20112540916799396], [u'dynamic', 0.20112540916799396], ['reentry', 0.20112540916799396], [u'combine', 0.20112540916799396], ['consideration', 0.20112540916799396], ['realistic', 0.20112540916799396], [u'effect', 0.20112540916799396], ['relative', 0.20112540916799396], ['simplicity', 0.20112540916799396], [u'result', 0.20112540916799396]]
[[618, 0.002940332328689092], [1175, 0.0028799686442782376], [1089, 0.002827352081316574], [879, 0.00264386507734697], [934, 0.00264386507734697], [1396, 0.00260524286568462], [263, 0.002474252177319734], [285, 0.002364077742211983], [631, 0.002290712397668609], [136, 0.0022467767593299364]]
[['structural', 0.2727411870290969], ['aeroelastic', 0.2727411870290969], [u'problem', 0.2727411870290969], [u'associate', 0.2727411870290969], ['flight', 0.2727411870290969], ['high', 0.2727411870290969], ['speed', 0.2727411870290969], ['aircraft', 0.2727411870290969]]
[[883, 0.014675778926103642], [1041, 0.011575390906491519], [1167, 0.01078863369094623], [252, 0.010315758955580652], [1164, 0.010215608076995775], [1168, 0.010022359659195063], [881, 0.009809089519486433], [414, 0.009570155634394886], [11, 0.009451267098052217], [908, 0.00926434041902758]]
[[u'have', 0.18039839878735509], ['anyone', 0.18039839878735509], ['formally', 0.18039839878735509], [u'determine', 0.18039839878735509], ['influence', 0.18039839878735509], ['joule', 0.18039839878735509], ['heating', 0.18039839878735509], [u'produce', 0.18039839878735509], ['induced', 0.18039839878735509], ['current', 0.18039839878735509], ['magnetohydrodynamic', 0.18039839878735509], ['free', 0.18039839878735509], ['convection', 0.18039839878735509], [u'flow', 0.18039839878735509], ['under', 0.18039839878735509], ['general', 0.18039839878735509], [u'condition', 0.18039839878735509]]
[[106, 0.004625794025070907], [319, 0.004478303219396933], [285, 0.004231598790737219], [477, 0.0038568115759456366], [297, 0.003731919349497445], [321, 0.003632383562525198], [1161, 0.0036189913429472502], [632, 0.003449637144089014], [550, 0.0034089354006866576], [1368, 0.0033756480627682426]]
[[u'problem', 0.2727411870290969], ['heat', 0.2727411870290969], ['conduction', 0.2727411870290969], ['composite', 0.2727411870290969], [u'slab', 0.2727411870290969], [u'solve', 0.2727411870290969], ['so', 0.2727411870290969], ['far', 0.2727411870290969]]
[[1140, 0.009833851457553706], [802, 0.008486231177910145], [653, 0.00834988746264576], [315, 0.00828335343449571], [272, 0.007695113624454735], [818, 0.007635915537058752], [1242, 0.007526040520427797], [1195, 0.007368835313199021], [1244, 0.0071217285212042585], [801, 0.007084382908243571]]
[['can', 0.1644591931838555], ['criterion', 0.1644591931838555], [u'develop', 0.1644591931838555], ['to', 0.1644591931838555], ['show', 0.1644591931838555], ['empirically', 0.1644591931838555], ['validity', 0.1644591931838555], ['flow', 0.1644591931838555], [u'solution', 0.1644591931838555], ['chemically', 0.1644591931838555], [u'react', 0.1644591931838555], ['gas', 0.1644591931838555], [u'mixture', 0.1644591931838555], [u'base', 0.1644591931838555], [u'simplify', 0.1644591931838555], ['assumption', 0.1644591931838555], ['instantaneous', 0.1644591931838555], ['local', 0.1644591931838555], ['chemical', 0.1644591931838555], ['equilibrium', 0.1644591931838555]]
[[1311, 0.007058651715944578], [302, 0.006545656756179044], [1188, 0.00643722212356808], [1285, 0.006276171623141186], [1010, 0.0062211324852657545], [850, 0.006105661420570817], [1066, 0.0060405458631668935], [743, 0.005994302626934519], [1251, 0.005735735351686665], [1009, 0.005727428706333745]]
[['chemical', 0.2727411870290969], ['kinetic', 0.2727411870290969], ['system', 0.2727411870290969], ['applicable', 0.2727411870290969], ['to', 0.2727411870290969], ['hypersonic', 0.2727411870290969], ['aerodynamic', 0.2727411870290969], [u'problem', 0.2727411870290969]]
[[319, 0.009679932593875238], [606, 0.008836529061324936], [180, 0.007851462109142147], [853, 0.007628551719060065], [532, 0.007495871133038507], [577, 0.0072149957658402975], [854, 0.007136140985442562], [1137, 0.007136140985442562], [550, 0.007039176656062785], [1028, 0.006945938411506153]]
[['theoretical', 0.24188650172516024], ['experimental', 0.24188650172516024], [u'guide', 0.24188650172516024], ['do', 0.24188650172516024], ['we', 0.24188650172516024], ['to', 0.24188650172516024], ['turbulent', 0.24188650172516024], ['couette', 0.24188650172516024], ['flow', 0.24188650172516024], ['behaviour', 0.24188650172516024]]
[[882, 0.01295862946794374], [864, 0.011527589606207655], [264, 0.009866301195667383], [129, 0.009710769331629393], [740, 0.009460104905616563], [848, 0.009134104690282493], [741, 0.00884859308945211], [736, 0.008700946028360893], [1362, 0.008540506992141875], [801, 0.008026336379185805]]
[['possible', 0.15567036432314413], ['to', 0.17609069405480451], ['relate', 0.15567036432314413], ['available', 0.15567036432314413], ['pressure', 0.17609069405480451], [u'distribution', 0.15567036432314413], ['ogive', 0.17609069405480451], ['forebody', 0.17609069405480451], ['at', 0.17609069405480451], ['zero', 0.15567036432314413], ['angle', 0.17609069405480451], ['attack', 0.17609069405480451], ['to', 0.17609069405480451], [u'low', 0.15567036432314413], ['surface', 0.15567036432314413], [u'pressure', 0.17609069405480451], ['equivalent', 0.15567036432314413], ['ogive', 0.17609069405480451], ['forebody', 0.17609069405480451], ['at', 0.17609069405480451], ['angle', 0.17609069405480451], ['attack', 0.17609069405480451]]
[[491, 0.009352196354836926], [707, 0.007007751952093751], [353, 0.006841937052493597], [1349, 0.006322955813635726], [1114, 0.00626322613572205], [47, 0.006105814864722308], [68, 0.00606159742273125], [247, 0.006031150686067071], [1005, 0.005762593331251698], [1076, 0.005616532784727212]]
[['methods', 0.20955340746286433], ['dash', 0.2347800830534691], ['exact', 0.20955340746286433], ['approximate', 0.20955340746286433], ['dash', 0.2347800830534691], ['presently', 0.20955340746286433], ['available', 0.20955340746286433], [u'predict', 0.20955340746286433], ['body', 0.20955340746286433], [u'pressure', 0.20955340746286433], ['at', 0.20955340746286433], ['angle', 0.20955340746286433], ['attack', 0.20955340746286433]]
[[491, 0.008396645795938419], [707, 0.006291742467222103], [353, 0.006142869525850262], [1349, 0.005676914634390669], [1114, 0.005623287771788791], [47, 0.005481959827343984], [68, 0.005442260254717996], [247, 0.0054149243804793076], [1005, 0.005173806583255924], [1076, 0.0050426696152758846]]
[[u'paper', 0.2928373394485904], ['internal', 0.2928373394485904], ['slip', 0.2928373394485904], ['flow', 0.2928373394485904], ['heat', 0.2928373394485904], ['transfer', 0.2928373394485904], [u'study', 0.2928373394485904]]
[[1151, 0.011591531201298348], [506, 0.009670644522421334], [548, 0.009140478594604578], [1268, 0.007839949256980438], [861, 0.007015822924273156], [715, 0.00666285455247982], [839, 0.006608015310844983], [577, 0.0064470963482808905], [1053, 0.006359038550302161], [406, 0.006037820708719219]]


################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################

TOP 5 DOCS FOR WEIGHTING SCHEME 2

1 ##################
[[470, 0.036948089523964174], [994, 0.036948089523964174], [883, 0.011194391414866568], [881, 0.010732540290294355], [1041, 0.009628395242222757]]
1 ['similarity', u'law', 'must', u'obey', u'construct', 'aeroelastic', u'model', 'heated', 'high', 'speed', 'aircraft']
1 0.036948089524 470 

1 0.036948089524 994 

1 0.0111943914149 883 
the estimation of fatigue damage on structural elements 

1 0.0107325402903 881 
the variation of gust frequency with gust velocity
and altitude 

1 0.00962839524222 1041 
on transverse vibrations of thin shallow elastic shells 

2 ##################
[[470, 0.03806191436880776], [994, 0.03806191436880776], [9, 0.010872683286511559], [618, 0.010696595976104823], [1149, 0.009690059344077278]]
2 ['realgas', 'transport', u'property', 'air', 'available', 'over', 'wide', 'range', u'enthalpy', u'density']
1 0.0380619143688 470 

1 0.0380619143688 994 

1 0.0108726832865 9 
the theory of the impact tube at low pressure 

1 0.0106965959761 618 
density of the upper atmosphere from analysis of satellite orbits 
further results 

1 0.00969005934408 1149 
preliminary results of density measurements from an air force satellite

3 ##################
[[470, 0.027502459317185774], [994, 0.027502459317185774], [506, 0.011307580674690454], [1151, 0.009786727921382554], [280, 0.008918320225034838]]
3 ['possible', 'to', 'find', 'analytical', 'similar', 'solution', 'strong', 'blast', 'wave', 'problem', 'newtonian', 'approximation']
1 0.0275024593172 470 

1 0.0275024593172 994 

1 0.0113075806747 506 
energy equation approximations in fluid mechanics 

1 0.00978672792138 1151 
on periodically oscillating wakes in the oseen approximation 

1 0.00891832022503 280 
higher order approximations for relaxation oscillations 

4 ##################
[[470, 0.02892253488799811], [994, 0.02892253488799811], [338, 0.008261948115200249], [1305, 0.008261948115200249], [202, 0.008257599297347436]]
4 ['can', 'aerodynamic', 'performance', 'channel', 'flow', 'ground', 'effect', u'machine', u'calculate']
1 0.028922534888 470 

1 0.028922534888 994 

1 0.0082619481152 338 
experimental evaluation of heat transfer with transpiration
cooling in a turbulent boundary layer at m 

1 0.0082619481152 1305 
experiments on circular cones at yaw in supersonic
flow 

1 0.00825759929735 202 
calculated velocity distributions and force derivatives
for a series of highspeed aerofoils 

5 ##################
[[470, 0.13982604894163822], [994, 0.13982604894163822], [1044, 0.03207829563216702], [506, 0.03126605504587156], [495, 0.029923956875003703]]
5 ['basic', 'mechanism', 'transonic', 'aileron', 'buzz']
1 0.139826048942 470 

1 0.139826048942 994 

1 0.0320782956322 1044 
the bending strength of pressurized cylinders 

1 0.0312660550459 506 
energy equation approximations in fluid mechanics 

1 0.029923956875 495 
a theory of transonic aileron buzz neglecting viscous
effects 


6 ##################
[[470, 0.06151020106261164], [994, 0.06151020106261164], [290, 0.018147795930724176], [325, 0.01786724888009195], [968, 0.016806241224630893]]
6 q9
1 0.0615102010626 470 

1 0.0615102010626 994 

1 0.0181477959307 290 
sweepback effects in the turbulent boundarylayer shockwave
interaction 

1 0.0178672488801 325 
forstorder slip effects on the compressible laminar
boundary layer over a slender body of revolution in
axial flow 

1 0.0168062412246 968 
on the use of sidejets as control devices 

7 ##################
[[470, 0.07366477771168488], [994, 0.07366477771168488], [760, 0.020567133607312944], [1098, 0.020368650251828047], [1095, 0.018232935887754067]]
7 q9
1 0.0736647777117 470 

1 0.0736647777117 994 

1 0.0205671336073 760 
buckling of sandwich under normal pressure 

1 0.0203686502518 1098 
a theoretical study of stagnation point ablation 

1 0.0182329358878 1095 
qualitative measurements of the effective heats of
ablation of several materials in supersonic air jets
at stagnation temperature up to  f

8 ##################
[[470, 0.04873619540245038], [994, 0.04873619540245038], [744, 0.01568740857633215], [1062, 0.013151989295686969], [110, 0.012407589935657859]]
8 q9
1 0.0487361954025 470 

1 0.0487361954025 994 

1 0.0156874085763 744 
an automatic method for finding the greatest or least
value function 

1 0.0131519892957 1062 
on obtaining solutions to the navierstokes equations
with high speed digital computers 

1 0.0124075899357 110 
the laminar boundary layer equation a method of solution
by means of an automatic computer 

9 ##################
[[470, 0.019012249117226633], [994, 0.019012249117226633], [319, 0.0077902291340837876], [606, 0.007021957450628024], [853, 0.006423808005764392]]
9 q9
1 0.0190122491172 470 

1 0.0190122491172 994 

1 0.00779022913408 319 
comment on improved numerical solution of the blasius problem with
threepoint boundary conditions 

1 0.00702195745063 606 
duct flow in magnetohydrodynamics 

1 0.00642380800576 853 
boundaryvalue problems of the thinwalled circular
cylinder 

10 ##################
[[470, 0.04046579227759276], [994, 0.04046579227759276], [905, 0.011372161333038873], [253, 0.010691793334422451], [290, 0.010387248819707472]]
10 q9
1 0.0404657922776 470 

1 0.0404657922776 994 

1 0.011372161333 905 
review of the pitot tube 

1 0.0106917933344 253 
boundary layers with suction and injection  a review
of published work on skin friction 

1 0.0103872488197 290 
sweepback effects in the turbulent boundarylayer shockwave
interaction 

11 ##################
[[470, 0.008068709674292008], [994, 0.008068709674292008], [1175, 0.0029243709918886497], [285, 0.0027262340968876616], [618, 0.0025971897128855186]]
11 q9
1 0.00806870967429 470 

1 0.00806870967429 994 

1 0.00292437099189 1175 
bending tests of ringstiffened circular cylinders 

1 0.00272623409689 285 
effect of roll on dynamic instability of symmetric
missiles 

1 0.00259718971289 618 
density of the upper atmosphere from analysis of satellite orbits 
further results 

12 ##################
[[470, 0.043876582178942865], [994, 0.043876582178942865], [883, 0.013293559726249885], [881, 0.01274510244245483], [1041, 0.011433908506222633]]
12 q9
1 0.0438765821789 470 

1 0.0438765821789 994 

1 0.0132935597262 883 
the estimation of fatigue damage on structural elements 

1 0.0127451024425 881 
the variation of gust frequency with gust velocity
and altitude 

1 0.0114339085062 1041 
on transverse vibrations of thin shallow elastic shells 

13 ##################
[[470, 0.014274897548358098], [994, 0.014274897548358098], [319, 0.0051566684166937], [285, 0.004823164297248891], [297, 0.004146517859284972]]
13 q9
1 0.0142748975484 470 

1 0.0142748975484 994 

1 0.00515666841669 319 
comment on improved numerical solution of the blasius problem with
threepoint boundary conditions 

1 0.00482316429725 285 
effect of roll on dynamic instability of symmetric
missiles 

1 0.00414651785928 297 
incompressible wedge flows of an electrically conducting
viscous fluid in the presence of a magnetic field 

14 ##################
[[470, 0.04694273771371997], [994, 0.04694273771371997], [1140, 0.012589481114367902], [1044, 0.010769402622486364], [506, 0.010496715257782093]]
14 q9
1 0.0469427377137 470 

1 0.0469427377137 994 

1 0.0125894811144 1140 
the wake behind an oscillating vehicle 

1 0.0107694026225 1044 
the bending strength of pressurized cylinders 

1 0.0104967152578 506 
energy equation approximations in fluid mechanics 

15 ##################
[[470, 0.026105416648631013], [994, 0.026105416648631013], [1010, 0.007336443773493601], [302, 0.006580227466743241], [1066, 0.006430502822933094]]
15 q9
1 0.0261054166486 470 

1 0.0261054166486 994 

1 0.00733644377349 1010 
freeflight measurements of the static and dynamic

1 0.00658022746674 302 
effect of variable heat recombination on stagnation
point heat transfer 

1 0.00643050282293 1066 
plastic stability theory of geometrically orthotropic
plates and cylindrical shells 

16 ##################
[[470, 0.022086300187330446], [994, 0.022086300187330446], [319, 0.009049815101968341], [606, 0.008157323165764167], [853, 0.007462460179555287]]
16 q9
1 0.0220863001873 470 

1 0.0220863001873 994 

1 0.00904981510197 319 
comment on improved numerical solution of the blasius problem with
threepoint boundary conditions 

1 0.00815732316576 606 
duct flow in magnetohydrodynamics 

1 0.00746246017956 853 
boundaryvalue problems of the thinwalled circular
cylinder 

17 ##################
[[470, 0.05273508594912185], [994, 0.05273508594912185], [129, 0.012339075910497878], [1044, 0.012098258443744939], [882, 0.01207002261350003]]
17 q9
1 0.0527350859491 470 

1 0.0527350859491 994 

1 0.0123390759105 129 
the behaviour of nonlinear systems 

1 0.0120982584437 1044 
the bending strength of pressurized cylinders 

1 0.0120700226135 882 
correlated fatigue data for aircraft structural joints 

18 ##################
[[470, 0.02500194133762479], [994, 0.02500194133762479], [491, 0.007687577530405407], [707, 0.006667587387496221], [1044, 0.005735838720159926]]
18 q9
1 0.0250019413376 470 

1 0.0250019413376 994 

1 0.00768757753041 491 
prediction of ogiveforebody pressures at angles of attack 

1 0.0066675873875 707 
aerodynamic characteristics of two winged reentry vehicles at supersonic
 and hypersonic speeds 

1 0.00573583872016 1044 
the bending strength of pressurized cylinders 

19 ##################
[[470, 0.029753088478686535], [994, 0.029753088478686535], [491, 0.009148456568238796], [707, 0.00793463654684328], [1044, 0.006825826628253627]]
19 q9
1 0.0297530884787 470 

1 0.0297530884787 994 

1 0.00914845656824 491 
prediction of ogiveforebody pressures at angles of attack 

1 0.00793463654684 707 
aerodynamic characteristics of two winged reentry vehicles at supersonic
 and hypersonic speeds 

1 0.00682582662825 1044 
the bending strength of pressurized cylinders 

20 ##################
[[470, 0.028719590997624347], [994, 0.028719590997624347], [506, 0.011808001910099048], [1151, 0.010843980243716859], [548, 0.008143872953477394]]
20 q9
1 0.0287195909976 470 

1 0.0287195909976 994 

1 0.0118080019101 506 
energy equation approximations in fluid mechanics 

1 0.0108439802437 1151 
on periodically oscillating wakes in the oseen approximation 

1 0.00814387295348 548 
experimental study of the velocity and temperature
distribution in a highvelocity vortextype flow 




 
3. 
 Weighting Scheme1 
  Q1     Relevant - > 883,1041          Non-Relvant->1167,252,1164
  Q2     Relevant - > 1102,1149,620,618 Non-Relvant->615
  Q3     Relevant - > 1151,506,280      Non-Relvant->919,1015
  Q4     Relevant - > 202,631           Non-Relvant->675,338,1305
  Q5     Relevant - > 496               Non-Relvant->0,1,2,3
  Q6     Relevant - > 290               Non-Relvant->968,972,1287,325
  Q7     Relevant - > 760,1095          Non-Relvant->1098,1116
  Q8     Relevant - > 744,110,1062      Non-Relvant->944,1005
  Q9     Relevant - > 319               Non-Relvant->606,180,853,532
  Q10    Relevant - > 290               Non-Relvant->905,727,253,608
  Q11    Relevant - > 618,934           Non-Relvant->1175,10889,879
  Q12    Relevant - > 883,1041          Non-Relvant->1167,252,1164
  Q13    Relevant - > 106,319,285       Non-Relvant->477,297
  Q14    Relevant - > 1140 ,802,653,315 Non-Relvant->272
  Q15    Relevant - > 1131,302,1188     Non-Relvant->1285,1010
  Q16    Relevant - > 319,606,180       Non-Relvant->853,532
  Q17    Relevant - > 882,864           Non-Relvant->264,129,740
  Q18    Relevant - > 491,707           Non-Relvant->353,1349,1114
  Q19    Relevant - > 491,707,353       Non-Relvant->1349,1114
  Q20    Relevant - > 1151,506,548,1268 Non-Relvant->861

Weighting Scheme 2
  Q1     Relevant - >883,81,1041        Non-Relvant->470,994
  Q2     Relevant - >9,618,1149         Non-Relvant->470,994
  Q3     Relevant - >506,1151,280       Non-Relvant->470,994
  Q4     Relevant - >338,1305,202       Non-Relvant->470,994
  Q5     Relevant - >1044,506           Non-Relvant->470,994,495
  Q6     Relevant - >290,325            Non-Relvant->470,994,968
  Q7     Relevant - >760,1098,1095      Non-Relvant->470,994
  Q8     Relevant - >744                Non-Relvant->470,994,1062,110
  Q9     Relevant - >319                Non-Relvant->470,994,606,853
  Q10    Relevant - >905,253            Non-Relvant->470,994,290
  Q11    Relevant - >1175,285           Non-Relvant->470,994,618
  Q12    Relevant - >883,881            Non-Relvant->470,994,1041
  Q13    Relevant - >319                Non-Relvant->470,994,285,297
  Q14    Relevant - >1140,1044          Non-Relvant->470,994,506
  Q15    Relevant - >1010               Non-Relvant->470,994,302,1066
  Q16    Relevant - >319,606            Non-Relvant->470,994,853
  Q17    Relevant - >129,1044,882       Non-Relvant->470,994
  Q18    Relevant - >491,707,1044       Non-Relvant->470,994
  Q19    Relevant - >491,707,1044       Non-Relvant->470,994
  Q20    Relevant - >506,1151,548       Non-Relvant->470,994


4. For all the queries the top-ranked non-relevant document did not get a
   low score because the  words with high weights corresponding to the query were
   present in the documents, but made little sense when manually opened and 
   checked w.r.t content.
   But although in almost all cases the top document is the most relevant and
   accurate.


5. The two weighting schemes provide almost the same results.
   the max-tf wwighting gives high weight to doc with high occurence in 
   the document while the okapi weighting focuses more on the document 
   length and gives high weight to the term present in the document whose
   length is nearer to the average document length of the collection.
   weighting scheme 2 i.e okapi gives results based on the parameter depending
   on the the whole collection while weighting scheme 1 i.e max-tf weighting 
   depends on the document only to give weighting.   


6. While calculating the weights for query and documents,i have chosen
   it to be a bit different. i have taken the idf parts in both the weighting
   schemes to be 1 while calcualting for the queries.
   Also i have increased the functions for retrieving the data for increase in 
   organiztion of the program but inturn increased the running time of the
   whole program.
    










