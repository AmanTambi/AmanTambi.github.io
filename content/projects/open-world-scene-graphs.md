---
title: Open-world scene graphs for manipulation
org: IIT Delhi
role: Co-first author
period: Nov 2023 – May 2024
venue: ICRA 2024 workshop
order: 3
featured: true
summary: Zero-shot scene graphs from foundation models, built for planners.
tags: [Foundation models, Scene understanding, Task planning]
highlights: []
media:
  type: video
  src: /media/scenegraph/rollout_clip.mp4
  poster: /media/scenegraph/rollout_clip.jpg
  alt: A Franka arm moves fruit into a basket while the scene graph updates
hero:
  type: video
  src: /media/scenegraph/rollout_clip.mp4
  poster: /media/scenegraph/rollout_clip.jpg
  caption: "\"Put all the fruits into the basket.\" The planner works from the graph, and the graph updates after every action."
links:
  - label: Paper
    url: https://openreview.net/pdf?id=IqRpVnq6mC
  - label: Poster
    url: https://drive.google.com/file/d/1EuoHcis_Ko9gonWzLNfNNA_aPYCY9CaB/view?usp=sharing
  - label: Project page
    url: https://reail-iitdelhi.github.io/scenegraph.github.io/
---

## The idea

A planner needs a scene representation that is open-set, structured and cheap to update. This one is built zero-shot from foundation models, with no priors about the scene.

<figure>
<img src="/media/scenegraph/overview.jpg" alt="Exploration and scene-graph generation, planning from the graph, plan rollout, and graph updates after each step" loading="lazy">
</figure>

## Pipeline

Objects are found and grounded. Relations come from focused questions to a vision-language model, checked against 3D poses. Everything is organised into spatial and category hierarchies, so the robot updates only the part of the graph an action changed.

<figure>
<img src="/media/scenegraph/pipeline.jpg" alt="Scene-graph generation pipeline" loading="lazy">
</figure>

## Results

Three views of one scene: spatio-depth relations, planar relations and category abstraction.

<figure>
<img src="/media/scenegraph/qualitative.jpg" alt="A workspace and the multi-hierarchy scene graph generated from it" loading="lazy">
</figure>

<figure class="tall">
<img src="/media/scenegraph/baselines.jpg" alt="Scene graphs from this method, from ConceptGraphs, and the ground truth, for the same scene" loading="lazy">
<figcaption>Top to bottom: the ground truth, ours, and ConceptGraphs, for the same scene.</figcaption>
</figure>
