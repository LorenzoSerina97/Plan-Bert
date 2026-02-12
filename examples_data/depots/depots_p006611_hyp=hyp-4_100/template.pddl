(define (problem depots-test)
(:domain depots)
(:objects
		depot0 - Depot
		depot1 - Depot
		depot2 - Depot
		distributor0 - Distributor
		distributor1 - Distributor
		distributor2 - Distributor
		truck0 - Truck
		truck1 - Truck
		truck2 - Truck
		pallet0 - Pallet
		pallet1 - Pallet
		pallet2 - Pallet
		pallet3 - Pallet
		pallet4 - Pallet
		pallet5 - Pallet
		crate0 - Crate
		crate1 - Crate
		crate2 - Crate
		hoist0 - Hoist
		hoist1 - Hoist
		hoist2 - Hoist
		hoist3 - Hoist
		hoist4 - Hoist
		hoist5 - Hoist
)
(:init

	(at pallet3 depot0)
	(clear pallet3)
	(at truck1 depot2)
	(clear crate0)
	(clear crate1)
	(available hoist0)
	(at pallet4 distributor1)
	(available hoist1)
	(available hoist2)
	(at hoist5 distributor2)
	(at pallet0 distributor0)
	(available hoist3)
	(at crate1 distributor1)
	(at truck0 distributor0)
	(on crate1 pallet4)
	(at pallet5 distributor2)
	(available hoist4)
	(at pallet2 depot2)
	(at crate2 depot1)
	(clear pallet5)
	(at hoist3 depot1)
	(at hoist4 depot0)
	(at truck2 depot0)
	(clear pallet0)
	(at hoist0 distributor1)
	(at crate0 depot2)
	(clear crate2)
	(at pallet1 depot1)
	(at hoist1 depot2)
	(on crate0 pallet2)
	(available hoist5)
	(at hoist2 distributor0)
	(on crate2 pallet1)
)
(:goal 
(and
<HYPOTHESIS>
))
)