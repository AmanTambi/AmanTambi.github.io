---
title: Perceptive locomotion for the Unitree A2
org: FieldAI
role: Research intern, locomotion
period: May – Aug 2026
order: 1
featured: true
summary: Teaching a quadruped to see the terrain and shape every step to it, from simulation to the real robot.
tags: [Legged locomotion, Reinforcement learning, Sim-to-real, Elevation mapping, MuJoCo]
media:
  type: video
  src: /media/a2/thumb_map.mp4
  poster: /media/a2/thumb_map.jpg
  alt: The robot's elevation map of a staircase building up as it climbs
hero:
  type: video
  src: /media/a2/s01_hero_grid6.mp4
  poster: /media/a2/s01_hero_grid6.jpg
  aspect: "1602 / 716"
  caption: "Top row: the real robot. Bottom row: the simulation the behaviours are trained in."
links: []
---
## The robot and the goal

The Unitree A2, with a LiDAR and three depth cameras on its payload. The goal: policies for stairs, slopes, rough ground and clutter, and a map built for the control loop.

<figure class="portrait-one">
<img src="/media/a2/a2_photo.jpg" alt="The Unitree A2 with its sensor payload" loading="lazy">
<figcaption>The A2 with its payload: a LiDAR and three depth cameras.</figcaption>
</figure>

## A trajectory generator, not end-to-end RL

A trajectory generator gives each leg a nominal plan: a phase clock, a swing arc, a stride length. The policy learns small residuals on top, the swing apex, joint fine-tuning and step timing. The learned part stays small, so the gait is natural from the start and transfers reliably to hardware.

<figure class="diagram narrow">
<img src="/media/a2/diagrams/tg.png" alt="A trotting quadruped with the trajectory generator's nominal plan dashed and the policy's residual corrections marked" loading="lazy">
</figure>

<figure class="grid-2">
<video data-autoplay muted loop playsinline preload="none" poster="/media/a2/s04_sim_blind.jpg"><source src="/media/a2/s04_sim_blind.mp4" type="video/mp4"></video>
<video data-autoplay muted loop playsinline preload="none" poster="/media/a2/s04_hw_blind.jpg"><source src="/media/a2/s04_hw_blind.mp4" type="video/mp4"></video>
<figcaption>The trajectory-generator gait in MuJoCo and on the robot, June 2026.</figcaption>
</figure>

## A map built for locomotion

Foot-scale detail, honest about unknown cells, fresh at control rate, robust to real sensors. Three inputs fused at two rates: the LiDAR point cloud at about 2 Hz for the wide field, depth cameras at about 15 Hz for the near field, foot contacts as ground truth. Output: a 6 m × 6 m grid at 5 cm, at 10 Hz.

<figure class="diagram">
<img src="/media/a2/diagrams/map.png" alt="Pipeline: point cloud, depth cameras and foot contacts fused per cell into a height grid the policy queries" loading="lazy">
</figure>

<figure>
<video data-autoplay muted loop playsinline preload="none" poster="/media/a2/map_full.jpg"><source src="/media/a2/map_full.mp4" type="video/mp4"></video>
<figcaption>The map building from recorded hardware data during a stair ascent. Colour is height.</figcaption>
</figure>

An offline experiment on top: a gated-convolution U-Net that fills stair occlusions and leaves uncertain cells blank. It halved the missing cells on descents. A belly camera did the same more cheaply.

## Teacher and student

The teacher trains in simulation with perfect terrain. The student, the policy that ships, sees proprioception and the noisy map, and learns by imitating the teacher step by step.

<figure class="diagram">
<img src="/media/a2/diagrams/distill.png" alt="Teacher trained in simulation with privileged perception supervises a student that sees proprioception and a noisy elevation map through a belief encoder" loading="lazy">
</figure>

## The belief encoder

Each foot's 52 height rays pass through a trust gate into a GRU memory, alongside proprioception. The policy acts on that memory. Trust has no labels: the gate learns to close on corrupted input because that is the only way to keep matching the teacher. A training-only decoder makes the memory reconstruct the true terrain.

<figure class="diagram">
<img src="/media/a2/diagrams/belief.png" alt="Noisy map heights pass through a trust gate into a recurrent belief, joined by proprioception; the policy acts on the belief; a training-only branch reconstructs the true terrain" loading="lazy">
</figure>

## Training against the map's real failures

Five corruptions, each fitted from real robot maps: per-ray jitter, whole-map drift, blind arcs, stale cells, and confident wrong fills. Every episode draws its own severity.

<figure class="diagram">
<img src="/media/a2/diagrams/noise.png" alt="One foot's 52 height rays as the teacher sees them, clean, and as the student sees them, with confident wrong fills marked" loading="lazy">
</figure>

## On the robot

July: live map in the loop, on stairs and a plank. The feet lift over the plank. Stairs were still bouncy and hesitant, which sent me back to the teacher.

<figure class="grid-2">
<video data-autoplay muted loop playsinline preload="none" poster="/media/a2/s12_hw_stair.jpg"><source src="/media/a2/s12_hw_stair.mp4" type="video/mp4"></video>
<video data-autoplay muted loop playsinline preload="none" poster="/media/a2/s12_hw_plank.jpg"><source src="/media/a2/s12_hw_plank.mp4" type="video/mp4"></video>
<figcaption>The perceptive student on hardware, July 2026.</figcaption>
</figure>

## The teacher under the microscope

Quarter-speed replays showed what full speed hid: airborne strides, feet on edges, calf strikes, bounce, crouching. Three root causes: cadence revved instead of placement fixed, no way to choose a foothold, and Isaac Sim registering 0.07% of edge strikes.

<figure class="grid-2">
<video data-autoplay muted loop playsinline preload="none" poster="/media/a2/s13_old_asc_slow.jpg"><source src="/media/a2/s13_old_asc_slow.mp4" type="video/mp4"></video>
<video data-autoplay muted loop playsinline preload="none" poster="/media/a2/s17_imp_asc.jpg"><source src="/media/a2/s17_imp_asc.mp4" type="video/mp4"></video>
<figcaption>Left: the old teacher at a quarter speed. Right: the rebuilt teacher at full speed.</figcaption>
</figure>

Training moved to MuJoCo and the gait was rebuilt:

- Duty cycle 0.5 → 0.6, so a pair of feet is always down.
- Touchdown arrives descending, not hovering.
- Footholds shift with velocity; cadence priced, not pinned.
- A ±6 cm foothold tool, then a 6 cm penalty band at the step nose.
- A riser penalty that grows before contact.

<figure class="diagram">
<img src="/media/a2/diagrams/gait.png" alt="Four panels: duty cycle overlap, touchdown arriving while descending, footholds shifted by velocity, and cadence priced rather than pinned" loading="lazy">
</figure>

<figure class="diagram">
<img src="/media/a2/diagrams/placement.png" alt="Foothold tool with a penalty band at the step nose, a riser penalty that grows before contact, and the Isaac Sim versus MuJoCo contact registration comparison" loading="lazy">
</figure>

| Mean over the evaluation suite | Old teacher | New teacher |
| --- | --- | --- |
| Vertical bounce (Vz RMS) | 0.142 m/s | 0.090 m/s |
| Time fully airborne | 0.8% | 0.0% |
| Riser kicks per metre | 5.4 | 2.7 |
| Calf strikes per metre | 2.3 | 0.8 |
| Loaded-foot slip | 144 mm/s | 78 mm/s |

## Scaling the terrain

Pyramid stairs with random commands made head-on climbs rare, so the teacher learned to shuffle. The fix: 550 scanned real staircases in seven shapes, with waypoints driven through the same velocity interface. Pyramids kept for lateral skills. Sixteen ground families, each with dials.

<figure class="grid-2">
<img src="/media/a2/stairs_straight_open.jpg" alt="The A2 climbing an open-riser straight staircase in MuJoCo with waypoints marked" loading="lazy">
<img src="/media/a2/stairs_curved_desc.jpg" alt="The A2 descending a curved staircase in MuJoCo with a waypoint trail" loading="lazy">
<figcaption>Scanned real staircases in MuJoCo, with the waypoint line the planner follows.</figcaption>
</figure>

<figure class="grid-4">
<img src="/media/a2/stairs/straight.png" alt="Straight staircase" loading="lazy">
<img src="/media/a2/stairs/l.png" alt="L-shaped staircase" loading="lazy">
<img src="/media/a2/stairs/u.png" alt="U-shaped staircase" loading="lazy">
<img src="/media/a2/stairs/spiral.png" alt="Spiral staircase" loading="lazy">
<figcaption>Four of the seven staircase shapes.</figcaption>
</figure>

<figure class="grid-6">
<img src="/media/a2/terr/cobble.jpg" alt="Cobble" loading="lazy">
<img src="/media/a2/terr/gravel.jpg" alt="Gravel" loading="lazy">
<img src="/media/a2/terr/rubble.jpg" alt="Rubble" loading="lazy">
<img src="/media/a2/terr/ruts.jpg" alt="Ruts" loading="lazy">
<img src="/media/a2/terr/corridor.jpg" alt="Corridor" loading="lazy">
<img src="/media/a2/terr/trench.jpg" alt="Trench" loading="lazy">
<img src="/media/a2/terr/curb_line.jpg" alt="Curbs" loading="lazy">
<img src="/media/a2/terr/wave.jpg" alt="Wave field" loading="lazy">
<img src="/media/a2/terr/clutter.jpg" alt="Clutter" loading="lazy">
<img src="/media/a2/terr/grid_islands.jpg" alt="Grid islands" loading="lazy">
<img src="/media/a2/terr/tilted_grid.jpg" alt="Tilted grid" loading="lazy">
<img src="/media/a2/terr/open_stairs.jpg" alt="Open-riser stairs" loading="lazy">
<figcaption>Twelve of the sixteen ground families, each a frame of the robot walking it.</figcaption>
</figure>

The student–teacher gap on riser kicks fell from 119% to 61%, with the same distillation in both generations.

<figure class="grid-3">
<video data-autoplay muted loop playsinline preload="none" poster="/media/a2/s22_old_student_asc.jpg"><source src="/media/a2/s22_old_student_asc.mp4" type="video/mp4"></video>
<video data-autoplay muted loop playsinline preload="none" poster="/media/a2/s22_comb_asc.jpg"><source src="/media/a2/s22_comb_asc.mp4" type="video/mp4"></video>
<video data-autoplay muted loop playsinline preload="none" poster="/media/a2/s22_teach_asc.jpg"><source src="/media/a2/s22_teach_asc.mp4" type="video/mp4"></video>
<figcaption>Left to right: the old student, the new student, and its teacher.</figcaption>
</figure>

<figure class="grid-4">
<video data-autoplay muted loop playsinline preload="none" poster="/media/a2/s22b_ruts.jpg"><source src="/media/a2/s22b_ruts.mp4" type="video/mp4"></video>
<video data-autoplay muted loop playsinline preload="none" poster="/media/a2/s22b_tilted_grid.jpg"><source src="/media/a2/s22b_tilted_grid.mp4" type="video/mp4"></video>
<video data-autoplay muted loop playsinline preload="none" poster="/media/a2/s22c_curved_up.jpg"><source src="/media/a2/s22c_curved_up.mp4" type="video/mp4"></video>
<video data-autoplay muted loop playsinline preload="none" poster="/media/a2/s22c_l_shaped_down.jpg"><source src="/media/a2/s22c_l_shaped_down.mp4" type="video/mp4"></video>
<figcaption>One student, one set of weights: ruts, tilted blocks, a curved ascent, an L-shaped descent.</figcaption>
</figure>

## What holds when the map goes away

Map disabled: the gate closes and the student climbs on memory and proprioception. Obstacle on the stairs: it sidesteps mid-climb.

<figure class="grid-2">
<video data-autoplay muted loop playsinline preload="none" poster="/media/a2/s23_blind_asc.jpg"><source src="/media/a2/s23_blind_asc.mp4" type="video/mp4"></video>
<video data-autoplay muted loop playsinline preload="none" poster="/media/a2/s23_obstacle.jpg"><source src="/media/a2/s23_obstacle.mp4" type="video/mp4"></video>
<figcaption>Left: no elevation map at all. Right: an obstacle on the staircase, seen from above.</figcaption>
</figure>

## What I learned

1. More information is not a better robot. It has to be added and used the right way, and the policy needs a mechanism to exploit it.
2. Decide the metrics on day one, with everyone in the room.
3. A paper is a proof of possibility, not a product.
