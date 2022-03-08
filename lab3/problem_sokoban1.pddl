;;#######
;;#@# $.#
;;#######

(define (problem simpleone)
  (:domain sokoban)
  (:objects
  teletransport - transport
  dir-right - direction
  dir-left - direction
  dir-up - direction
  dir-down - direction
  player-01 - player
  box-01 - box
  pos-1-1 - position
  pos-1-2 - position
  pos-1-3 - position
  pos-1-4 - position
  pos-1-5 - position
  pos-1-6 - position
  pos-1-7 - position
  pos-2-1 - position
  pos-2-2 - position
  pos-2-3 - position
  pos-2-4 - position
  pos-2-5 - position
  pos-2-6 - position
  pos-2-7 - position
  pos-3-1 - position
  pos-3-2 - position
  pos-3-3 - position
  pos-3-4 - position
  pos-3-5 - position
  pos-3-6 - position
  pos-3-7 - position
  )
  (:init 
  (is-goal pos-2-6)
  (at box-01 pos-2-5)
  (at player-01 pos-2-2)
  (is-transported teletransport)
  (transport-position pos-2-4)
  (transport-position pos-2-6)
  (non-goal pos-1-1)
  (non-goal pos-1-2)
  (non-goal pos-1-3)
  (non-goal pos-1-4)
  (non-goal pos-1-5)
  (non-goal pos-1-6)
  (non-goal pos-1-7)
  (non-goal pos-2-1)
  (non-goal pos-2-2)
  (non-goal pos-2-3)
  (non-goal pos-2-4)
  (non-goal pos-2-5)
  (non-goal pos-2-7)
  (non-goal pos-3-1)
  (non-goal pos-3-2)
  (non-goal pos-3-3)
  (non-goal pos-3-4)
  (non-goal pos-3-5)
  (non-goal pos-3-6)
  (non-goal pos-3-7)
  (empty pos-2-4)
  (empty pos-2-6)
  (direction-move pos-2-4 pos-2-5 dir-right)
  (direction-move pos-2-6 pos-2-5 dir-left)
  (direction-move pos-2-5 pos-2-4 dir-left)
  (direction-move pos-2-5 pos-2-6 dir-right)
  )
  (:goal (and 
  (at-goal box-01))
  )
)