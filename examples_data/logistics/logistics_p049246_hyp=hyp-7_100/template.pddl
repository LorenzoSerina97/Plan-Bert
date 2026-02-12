(define (problem logistics-test)
(:domain logistics)
(:objects
	apn1 apn2 apn3 apn4 apn5 apn6 - airplane
	cit1 cit2 cit3 cit4 cit5 cit6 - city
	apt1 apt2 apt3 apt4 apt5 apt6 - airport
	tru1 tru2 tru3 tru4 tru5 - truck
	obj00 obj11 obj12 obj13 obj21 obj22 obj23 obj33 obj44 obj55 - package
	pos11 pos12 pos13 pos21 pos22 pos23 pos33 pos44 pos55 pos66 - location
)
(:init
	(at apn1 apt3)
	(at apn2 apt5)
	(at apn3 apt1)
	(at apn4 apt5)
	(at apn5 apt5)
	(at apn6 apt5)
	(at obj00 pos23)
	(at obj11 pos22)
	(at obj12 pos22)
	(at obj13 pos33)
	(at obj21 pos23)
	(at obj22 pos55)
	(at obj23 pos22)
	(at obj33 pos55)
	(at obj44 pos12)
	(at obj55 pos13)
	(in-city apt1 cit2)
	(in-city apt2 cit4)
	(in-city apt3 cit5)
	(in-city apt4 cit3)
	(in-city apt5 cit1)
	(in-city apt6 cit6)
	(in-city pos11 cit3)
	(in-city pos12 cit6)
	(in-city pos13 cit4)
	(in-city pos21 cit6)
	(in-city pos22 cit1)
	(in-city pos23 cit6)
	(in-city pos33 cit5)
	(in-city pos44 cit1)
	(in-city pos55 cit5)
	(in-city pos66 cit4)
	(at tru5 pos11)
	(at tru4 pos12)
	(at tru3 pos13)
	(at tru2 pos44)
	(at tru1 pos33)
)
(:goal 
(and
<HYPOTHESIS>
))
)