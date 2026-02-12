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
	(at hoist2 depot1)
	(clear crate0)
	(at crate4 depot1)
	(available hoist0)
	(clear crate1)
	(clear crate5)
	(at pallet2 distributor0)
	(available hoist1)
	(at crate3 depot1)
	(on crate3 crate4)
	(available hoist2)
	(on crate4 crate2)
	(at truck1 distributor0)
	(at truck0 distributor0)
	(at crate2 depot1)
	(on crate2 pallet0)
	(at crate5 depot0)
	(at hoist0 depot0)
	(on crate1 pallet2)
	(at hoist1 distributor0)
	(at crate1 distributor0)
	(at pallet1 depot0)
	(on crate5 pallet1)
	(on crate0 crate3)
	(at crate0 depot1)
)
(:goal 
(and
<HYPOTHESIS>
))
)