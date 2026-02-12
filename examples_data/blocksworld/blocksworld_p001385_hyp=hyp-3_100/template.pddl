(define (problem blocksworld-test)
(:domain blocksworld)
(:objects
	A C H K R S T U 
)
(:init
	(on-table K)
	(arm-empty)
	(on-table C)
	(on T A)
	(on-table H)
	(on R T)
	(on U H)
	(clear R)
	(on A U)
	(clear C)
	(on-table S)
	(clear K)
	(clear S)
)
(:goal 
(and
<HYPOTHESIS>
))
)