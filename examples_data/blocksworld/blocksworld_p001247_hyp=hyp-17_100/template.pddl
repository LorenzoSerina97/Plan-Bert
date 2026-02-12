(define (problem blocksworld-test)
(:domain blocksworld)
(:objects
	A C H K R S T U 
)
(:init
	(arm-empty)
	(on-table R)
	(on-table U)
	(on-table H)
	(clear A)
	(on K H)
	(on A C)
	(clear S)
	(on-table T)
	(on S T)
	(clear K)
	(clear U)
	(on C R)
)
(:goal 
(and
<HYPOTHESIS>
))
)