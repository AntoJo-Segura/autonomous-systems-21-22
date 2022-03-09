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
  pos-0-0 - position
  pos-0-1 - position
  pos-0-2 - position
  pos-0-3 - position
  pos-0-4 - position
  pos-0-5 - position
  pos-0-6 - position
  pos-1-0 - position
  pos-1-1 - position
  pos-1-2 - position
  pos-1-3 - position
  pos-1-4 - position
  pos-1-5 - position
  pos-1-6 - position
  pos-2-0 - position
  pos-2-1 - position
  pos-2-2 - position
  pos-2-3 - position
  pos-2-4 - position
  pos-2-5 - position
  pos-2-6 - position
  )
  (:init 
  (is-goal pos-1-5)
  (at box-01 pos-1-4)
  (at player-01 pos-1-1)
  (is-transported teletransport)
  (transport-position pos-1-3)
  (transport-position pos-1-5)
  (non-goal pos-0-0)
  (non-goal pos-0-1)
  (non-goal pos-0-2)
  (non-goal pos-0-3)
  (non-goal pos-0-4)
  (non-goal pos-0-5)
  (non-goal pos-0-6)
  (non-goal pos-1-0)
  (non-goal pos-1-1)
  (non-goal pos-1-2)
  (non-goal pos-1-3)
  (non-goal pos-1-4)
  (non-goal pos-1-6)
  (non-goal pos-2-0)
  (non-goal pos-2-1)
  (non-goal pos-2-2)
  (non-goal pos-2-3)
  (non-goal pos-2-4)
  (non-goal pos-2-5)
  (non-goal pos-2-6)
  (empty pos-1-3)
  (empty pos-1-5)
  (direction-move pos-1-3 pos-1-4 dir-right)
  (direction-move pos-1-5 pos-1-4 dir-left)
  (direction-move pos-1-4 pos-1-5 dir-right)
  (direction-move pos-1-4 pos-1-3 dir-left)
  )
  (:goal (and 
  (at-goal box-01)
  ))
)