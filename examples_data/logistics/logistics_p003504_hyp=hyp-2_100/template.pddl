(define (problem logistics-test)
(:domain logistics)
(:objects
	apn1 - airplane
	cit1 cit2 - city
	apt1 apt2 - airport
	tru1 tru2 - truck
	obj11 obj12 obj13 obj21 obj22 obj23 - package
	pos11 pos12 pos13 pos21 pos22 pos23 - location
)
(:init
	(at apn1 apt2)
	(at obj11 pos12)
	(at obj12 pos23)
	(at obj13 pos22)
	(at obj21 pos21)
	(at obj22 pos23)
	(at obj23 pos21)
	(in-city apt1 cit1)
	(in-city apt2 cit2)
	(in-city pos11 cit1)
	(in-city pos12 cit1)
	(in-city pos13 cit1)
	(in-city pos21 cit2)
	(in-city pos22 cit1)
	(in-city pos23 cit1)
	(at tru2 pos13)
	(at tru1 pos21)
)
(:goal 
(and
<HYPOTHESIS>
))
)