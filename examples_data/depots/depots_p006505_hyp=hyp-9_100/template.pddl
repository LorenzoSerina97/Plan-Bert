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

	(on crate1 pallet3)
	(clear pallet2)
	(clear crate0)
	(on crate0 pallet0)
	(clear crate1)
	(available hoist0)
	(at hoist5 depot1)
	(available hoist1)
	(available hoist2)
	(at pallet3 depot1)
	(at truck2 distributor0)
	(at pallet0 depot2)
	(at pallet4 distributor0)
	(available hoist3)
	(at hoist2 distributor2)
	(at pallet5 distributor2)
	(at pallet2 distributor1)
	(available hoist4)
	(at truck1 distributor1)
	(at hoist1 distributor0)
	(at hoist4 depot0)
	(at hoist0 distributor1)
	(at crate0 depot2)
	(at hoist3 depot2)
	(at pallet1 depot0)
	(clear crate2)
	(at crate2 distributor2)
	(at truck0 distributor1)
	(clear pallet4)
	(available hoist5)
	(clear pallet1)
	(at crate1 depot1)
	(on crate2 pallet5)
)
(:goal 
(and
<HYPOTHESIS>
))
)