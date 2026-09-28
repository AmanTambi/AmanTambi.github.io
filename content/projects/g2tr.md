---
title: "G²TR: grounded temporal reasoning"
org: IIT Delhi
role: Co-author
period: Jan – Sep 2024
venue: arXiv
order: 5
featured: false
summary: A robot that understands "remove the cloth I used to wipe the table".
result: 70.1% grounding accuracy, 26 points over the strongest baseline.
tags: [Foundation models, Video grounding, Manipulation, Instruction following]
highlights: []
media:
  type: video
  src: /media/g2tr/demo1.mp4
  poster: /media/g2tr/demo1.jpg
  alt: A person places a banana on a table in front of a Franka arm
hero:
  type: video
  src: /media/g2tr/demo4.mp4
  poster: /media/g2tr/demo4.jpg
  caption: "\"Robot, remove the cloth that was used to wipe the table.\""
links:
  - label: arXiv
    url: https://arxiv.org/abs/2410.07494
  - label: Code
    url: https://github.com/Project-LPEA/embodied_temporal_reasoning
  - label: Project page
    url: https://reail-iitdelhi.github.io/temporalreasoning.github.io/
---

## The problem

To act on an instruction about the past, the robot has to find the moment, work out which object was involved, and know where that object is now.

## Pipeline

An LLM splits the instruction into "when" and "what". The event localizer finds the moment, the target detector picks the object, and the tracker follows it to now. If the object is hidden, the detector re-targets whatever is hiding it.

<figure>
<img src="/media/g2tr/pipeline.png" alt="Pipeline: video and instruction into an event localizer, then a target detector, then an object tracker with a loop back when the target is occluded, then a motion planner and robot execution" loading="lazy">
</figure>

## The dataset

155 videos of people handling objects in front of a Franka, each paired with an instruction that refers back to them.

<figure class="grid-4">
<video data-autoplay muted loop playsinline preload="none" poster="/media/g2tr/single_hop.jpg"><source src="/media/g2tr/single_hop.mp4" type="video/mp4"></video>
<video data-autoplay muted loop playsinline preload="none" poster="/media/g2tr/multi_hop.jpg"><source src="/media/g2tr/multi_hop.mp4" type="video/mp4"></video>
<video data-autoplay muted loop playsinline preload="none" poster="/media/g2tr/spatially_complex.jpg"><source src="/media/g2tr/spatially_complex.mp4" type="video/mp4"></video>
<video data-autoplay muted loop playsinline preload="none" poster="/media/g2tr/partially_obs.jpg"><source src="/media/g2tr/partially_obs.mp4" type="video/mp4"></video>
<figcaption>"Pick the cloth I just dropped." "Give me the object placed second." "Point to the cup that was just placed." "Where is the medicine?"</figcaption>
</figure>

## On the robot

<figure class="grid-3">
<video data-autoplay muted loop playsinline preload="none" poster="/media/g2tr/demo1.jpg"><source src="/media/g2tr/demo1.mp4" type="video/mp4"></video>
<video data-autoplay muted loop playsinline preload="none" poster="/media/g2tr/demo2.jpg"><source src="/media/g2tr/demo2.mp4" type="video/mp4"></video>
<video data-autoplay muted loop playsinline preload="none" poster="/media/g2tr/demo3.jpg"><source src="/media/g2tr/demo3.mp4" type="video/mp4"></video>
<figcaption>"Pick the object I just placed." "Where is the marker I just used?" "Give me the bottle placed second."</figcaption>
</figure>

## What breaks

Most failures come from finding the wrong moment in the video, not from picking the wrong object.

<figure class="tall">
<img src="/media/g2tr/failures.png" alt="Breakdown of 45 failures: 62% event localisation, 29% target detection, 9% tracking" loading="lazy">
</figure>
