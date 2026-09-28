---
title: Foundation-model priors for 3D object models
org: IIT Delhi
role: Co-author
period: 2024
venue: ICRA 2024 workshop
order: 9
featured: false
summary: Better 3D models of unknown objects, so a robot can grasp and place things it has never seen.
tags: [3D perception, Foundation models]
highlights: []
media:
  type: image
  src: /media/3dobj/qualitative_tile.jpg
  alt: 3D models of a helmet, a case, a tree branch and a truss, unfiltered, from this method, and ground truth
hero:
  type: image
  src: /media/3dobj/motivation.jpg
  alt: "\"Put the briefcase inside the crate.\" With the full object model the task succeeds; with a partial model it fails."
  aspect: "1145 / 516"
  caption: "\"Put the briefcase inside the crate.\" A partial object model makes the placement fail. A complete one makes it work."
links:
  - label: Paper
    url: https://openreview.net/pdf?id=s86mu1ovz4
  - label: Poster
    url: https://drive.google.com/file/d/1nMaZVEe26TRL3rwZ8TiOOYyyabFefAf2/view?usp=sharing
  - label: Project page
    url: https://reail-iitdelhi.github.io/3DObjectModels.github.io/
---

## The problem

To move large, unfamiliar objects like trusses, tree branches or a briefcase, a robot needs an accurate 3D model of each one, not just a label.

## Approach

Posed RGB-D images build a global point cloud. Depth priors from a foundation model clean up the noisy depth, a vision-language model segments every object, and the masks cut each object's model out of the cloud.

<figure class="diagram">
<img src="/media/3dobj/methodology.jpg" alt="Pipeline: posed RGB-D images, guided depth filtering with foundation-model depth priors, semantic masks from a vision-language model, fused into per-object 3D models" loading="lazy">
</figure>

## Results

Cleaner and more complete models than masking the raw point cloud, with lower error against the ground truth on every object but one.

<figure class="diagram">
<img src="/media/3dobj/qualitative.jpg" alt="Helmet, case, tree branch and truss: unfiltered models, models from this method, and ground truth" loading="lazy">
</figure>

<figure class="diagram narrow">
<img src="/media/3dobj/accuracy.png" alt="Reconstruction accuracy against distance threshold, and RMSE per object, for the unfiltered and proposed methods" loading="lazy">
</figure>

## Local updates

After each action the robot rebuilds only the area it touched. Moving the briefcase here reveals the hose underneath, which then gets its own model.

<figure class="diagram">
<img src="/media/3dobj/rollout.jpg" alt="Plan rollout: pick the briefcase, locally update the scene, pick the hose that was hidden underneath, update again" loading="lazy">
</figure>
