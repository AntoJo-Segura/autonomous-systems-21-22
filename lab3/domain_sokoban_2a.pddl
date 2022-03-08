(define (domain sokoban)
  (:requirements :typing )
  (:types 
        thing position direction transport - object 
        player box - element)

  (:predicates (empty ?e - position) ;;cell is empty
               (transport-position ?p - position) ;; place to teletransport
               (is-transported ?t - transport) ;;transport flag
	       (at ?t - thing ?p - position) ;; place where it is a thing
	       (at-goal ?b - box) ;;box at goal cell
	       (is-goal ?p - position);; goal cell
               (non-goal ?p - position);; not at goal
               (direction-move ?from ?to - position ?dir - direction)) ;; direction of movement from -to
  

  (:action move
   :parameters (?x - player ?from ?to - position ?dir - direction)
   :precondition (and (at ?x ?from)
                      (empty ?to)
                      (direction-move ?from ?to ?dir))
   :effect       (and (not (at ?x ?from))
                      (not (empty ?to))
                      (at ?x ?to)
                      (empty ?from)
                      (transport-position ?from)
                      (not (transport-position ?to)))
   )

  (:action teletransport
   :parameters (?x - player ?from ?to - position ?t - transport)
   :precondition (and (at ?x ?from)
                      (empty ?to)
                      (transport-position ?to)
                      (is-transported ?t))
   :effect       (and (not (at ?x ?from))
                      (not (empty ?to))
                      (not (transport-position ?to))
                      (transport-position ?from)
                      (at ?x ?to)
                      (empty ?from)
                      (not(is-transported ?t)))
   )

  (:action push-to-nongoal
   :parameters (?x - player ?b - box
                ?xpos ?from ?to - position
                ?dir - direction)
   :precondition (and (at ?x ?xpos)
                      (at ?b ?from)
                      (empty ?to)
                      (direction-move ?xpos ?from ?dir)
                      (direction-move ?from ?to ?dir)
                      (non-goal ?to))
   :effect       (and (not (at ?x ?xpos))
                      (not (at ?b ?from))
                      (not (empty ?to))
                      (at ?x ?from)
                      (at ?b ?to)
                      (empty ?xpos)
                      (transport-position ?xpos)
                      (not (at-goal ?b)))
   )

  (:action push-to-goal
   :parameters (?x - player ?b - box
                ?xpos ?from ?to - position
                ?dir - direction)
   :precondition (and (at ?x ?xpos)
                      (at ?b ?from)
                      (empty ?to)
                      (direction-move ?xpos ?from ?dir)
                      (direction-move ?from ?to ?dir)
                      (is-goal ?to))
   :effect       (and (not (at ?x ?xpos))
                      (not (at ?b ?from))
                      (not (empty ?to))
                      (at ?x ?from)
                      (at ?b ?to)
                      (empty ?xpos)
                      (transport-position ?xpos)
                      (at-goal ?b))
  )
)