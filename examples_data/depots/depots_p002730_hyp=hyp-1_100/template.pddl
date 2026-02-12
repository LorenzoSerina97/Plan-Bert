(define (problem depots-test)
(:domain depots)
(:objects
		depot0 - Depot
		depot1 - Depot
		distributor0 - Distributor
		truck0 - Truck
		truck1 - Truck
		pallet0 - Pallet
		pallet1 - Pallet
		pallet2 - Pallet
		crate0 - Crate
		crate1 - Crate
		crate2 - Crate
		crate3 - Crate
		crate4 - Crate
		crate5 - Crate
		hoist0 - Hoist
		hoist1 - Hoist
		hoist2 - Hoist
)
(:init

	(at pallet0 depot1)
	(at truck1 depot1)
	(on crate4 pallet1)
	(at crate3 depot0)
	(on crate2 crate4)
	(clear crate0)
	(at hoist1 depot1)
	(on crate0 pallet0)
	(available hoist0)
	(clear crate5)
	(available hoist1)
	(available hoist2)
	(at pallet2 depot0)
	(at crate2 distributor0)
	(at crate1 depot0)
	(at truck0 distributor0)
	(at crate4 distributor0)
	(at pallet1 distributor0)
	(at crate5 depot0)
	(at hoist0 depot0)
	(on crate1 pallet2)
	(on crate5 crate3)
	(clear crate2)
	(on crate3 crate1)
	(at hoist2 distributor0)
	(at crate0 depot1)
)
(:goal 
(and
<HYPOTHESIS>
))
)