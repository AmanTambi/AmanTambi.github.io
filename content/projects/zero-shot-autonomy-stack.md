---
title: Zero-shot task planning for assistive robots
org: IIT Delhi
role: Project Scientist
period: Jun 2023 – Dec 2024
order: 7
featured: false
summary: A robot that takes an instruction, plans from what it sees, and carries it out in a scene it has never seen.
tags: [Systems, LLM planning, Manipulation]
highlights: []
media:
  type: video
  src: /media/taskplan/medicine.mp4
  poster: /media/taskplan/medicine.jpg
  alt: A Franka arm hands a pill box to a seated person
hero:
  type: video
  src: /media/taskplan/medicine.mp4
  poster: /media/taskplan/medicine.jpg
  caption: "\"It's time for my medicine, give me the pill box.\" It hands over the pill box, then a cup and a bottle of water."
links:
  - label: Full video
    url: https://drive.google.com/file/d/1Qpc4blP0bpEBzy3m2TczPmLotGx562kW/view?usp=sharing
---

## The system

An assistive robot has to understand an instruction, look at whatever scene it is in, and work out the steps itself. This ROS stack builds a scene graph of the table, plans with an LLM over the instruction and the graph, and executes skills like pick, place, give and unstack. Every action is checked, so a failure becomes a re-plan.

<figure>
<video data-autoplay muted loop playsinline preload="none" poster="/media/taskplan/explore.jpg"><source src="/media/taskplan/explore.mp4" type="video/mp4"></video>
<figcaption>First, the robot explores the table and builds its scene graph.</figcaption>
</figure>

## Instructions it has never seen

<figure class="grid-2">
<video data-autoplay muted loop playsinline preload="none" poster="/media/taskplan/cloth.jpg"><source src="/media/taskplan/cloth.mp4" type="video/mp4"></video>
<video data-autoplay muted loop playsinline preload="none" poster="/media/taskplan/vegetables.jpg"><source src="/media/taskplan/vegetables.mp4" type="video/mp4"></video>
<figcaption>Left: "Put the cloth in the bin." The carrot is on the cloth, so it moves the carrot first. Right: "Put all vegetables into the basket." It finds the carrot and the capsicum itself.</figcaption>
</figure>

<figure>
<video data-autoplay muted loop playsinline preload="none" poster="/media/taskplan/spectacles.jpg"><source src="/media/taskplan/spectacles.mp4" type="video/mp4"></video>
<figcaption>"Put the spectacles near the tray but not inside it." It works out a placing region from the description.</figcaption>
</figure>

Also ran on a Hello Robot Stretch.
