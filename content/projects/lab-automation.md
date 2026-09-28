---
title: Wet-lab automation with a mobile manipulator
org: Carnegie Mellon University
role: MRSD capstone
period: Aug 2025 – May 2027
order: 4
featured: true
summary: A mobile manipulator that moves well plates between lab instruments, with a gripper and pick-and-place strategies built around contact.
tags: [Mobile manipulation, Contact-rich manipulation, Force control, Navigation]
media:
  type: video
  src: /media/lab/thumb_nav.mp4
  poster: /media/lab/thumb_nav.jpg
  alt: The mobile manipulator driving up to an instrument in the lab
hero:
  type: image
  src: /media/lab/arm_gripper.jpg
  alt: The xArm with a wrist camera and the custom two-finger gripper on the bench
  aspect: "16 / 10"
  caption: The arm with its wrist camera and the custom gripper.
links: []
---
## The task

A mobile base with a 6-DoF xArm moves well plates between lab instruments. The holders leave about two millimetres of clearance. Mine: the gripper, picking, placing, navigation.

## The gripper

Two fingers on a rack and pinion, one Dynamixel servo, built from scratch for the plate's skirt.

<figure class="grid-2 gripper">
<img src="/media/lab/gripper_photo.jpg" alt="The rack-and-pinion gripper mounted on the arm, wrist camera above it" loading="lazy">
<img class="cad" src="/media/lab/gripper_cad.png" alt="CAD render of the two-finger gripper" loading="lazy">
</figure>

## Picking

Vision gets the fingers around the plate to within a centimetre, so the plate is never centred. The arm goes soft before the fingers close: the first finger to touch pushes the arm, not the plate, and the gripper centres itself.

<figure class="anim">
<svg viewBox="0 30 1000 370" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Two panels. The fingers are already around an off-centre plate and close. With position control the first finger to touch shoves the plate off its stand. With low stiffness the plate stays put, the arm yields sideways until the second finger arrives, and the grasp is centred.">
<style>
.pk-t{font-size:19px;font-weight:600;fill:#111111}
.pk-s{font-size:17px;fill:#555555}
.pk-ok{font-size:19px;font-weight:600;fill:#111111}
.pk-body{fill:#fff;stroke:#111111;stroke-width:2.5}
.pk-plate{fill:#d9d9d9;stroke:#111111;stroke-width:2.5}
.pk-stand{fill:#ececec;stroke:#555555;stroke-width:2}
.pk-line{stroke:#555555;stroke-width:2}
.pk-acc{fill:none;stroke:#111111;stroke-width:4;stroke-linecap:round;stroke-linejoin:round}
#pkA-l{animation:pkA-l 8s ease-in-out infinite}
#pkA-r{animation:pkA-r 8s ease-in-out infinite}
#pkA-p{animation:pkA-p 8s ease-in-out infinite;transform-box:fill-box;transform-origin:0% 100%}
#pkA-x{animation:pk-late 8s linear infinite}
#pkB-g{animation:pkB-g 8s ease-in-out infinite}
#pkB-l{animation:pkB-l 8s ease-in-out infinite}
#pkB-r{animation:pkB-r 8s ease-in-out infinite}
#pkB-p{animation:pkB-p 8s ease-in-out infinite}
#pkB-a{animation:pkB-a 8s linear infinite}
#pkB-ok{animation:pk-late 8s linear infinite}
@keyframes pkA-l{0%,10%{transform:translateX(0)}22%{transform:translateX(10px)}46%,100%{transform:translateX(50px)}}
@keyframes pkA-r{0%,10%{transform:translateX(0)}22%{transform:translateX(-10px)}46%,100%{transform:translateX(-50px)}}
@keyframes pkA-p{0%,22%{transform:translate(0,0) rotate(0)}46%{transform:translate(-40px,0) rotate(0)}54%{transform:translate(-95px,10px) rotate(-24deg)}62%,100%{transform:translate(-130px,22px) rotate(0)}}
@keyframes pkB-g{0%,22%{transform:translate(0,0)}40%,50%{transform:translate(30px,0)}70%,100%{transform:translate(30px,-110px)}}
@keyframes pkB-l{0%,10%{transform:translateX(0)}22%{transform:translateX(10px)}40%,100%{transform:translateX(40px)}}
@keyframes pkB-r{0%,10%{transform:translateX(0)}22%{transform:translateX(-10px)}40%,100%{transform:translateX(-40px)}}
@keyframes pkB-p{0%,50%{transform:translateY(0)}70%,100%{transform:translateY(-110px)}}
@keyframes pkB-a{0%,22%{opacity:0}26%,38%{opacity:1}42%,100%{opacity:0}}
@keyframes pk-late{0%,64%{opacity:0}70%,100%{opacity:1}}
</style>
<g transform="translate(10,0)">
<line class="pk-line" x1="30" y1="300" x2="450" y2="300"/>
<rect class="pk-stand" x="225" y="278" width="90" height="22" rx="3"/>
<g id="pkA-p"><rect class="pk-plate" x="210" y="256" width="120" height="22" rx="4"/></g>
<rect class="pk-body" x="150" y="130" width="180" height="50" rx="8"/>
<g id="pkA-l"><rect class="pk-body" x="128" y="180" width="12" height="92" rx="2"/></g>
<g id="pkA-r"><rect class="pk-body" x="340" y="180" width="12" height="92" rx="2"/></g>
<text id="pkA-x" class="pk-t" x="30" y="60">Missed</text>
<text class="pk-t" x="30" y="352">Position control</text>
<text class="pk-s" x="30" y="378">The first finger to touch shoves the plate.</text>
</g>
<g transform="translate(510,0)">
<line class="pk-line" x1="30" y1="300" x2="450" y2="300"/>
<rect class="pk-stand" x="225" y="278" width="90" height="22" rx="3"/>
<g id="pkB-p"><rect class="pk-plate" x="210" y="256" width="120" height="22" rx="4"/></g>
<g id="pkB-g">
<rect class="pk-body" x="150" y="130" width="180" height="50" rx="8"/>
<g id="pkB-l"><rect class="pk-body" x="128" y="180" width="12" height="92" rx="2"/></g>
<g id="pkB-r"><rect class="pk-body" x="340" y="180" width="12" height="92" rx="2"/></g>
</g>
<g id="pkB-a"><path class="pk-acc" d="M76 155 H126 M112 143 L126 155 L112 167"/></g>
<text id="pkB-ok" class="pk-ok" x="30" y="60">Grasped</text>
<text class="pk-t" x="30" y="352">Low stiffness</text>
<text class="pk-s" x="30" y="378">The plate stays. The arm yields until both fingers touch.</text>
</g>
</svg>
</figure>

<figure class="pair-portrait">
<video data-autoplay muted loop playsinline preload="none" poster="/media/lab/grasp_stiff.jpg"><source src="/media/lab/grasp_stiff.mp4" type="video/mp4"></video>
<video data-autoplay muted loop playsinline preload="none" poster="/media/lab/grasp_compliant.jpg"><source src="/media/lab/grasp_compliant.mp4" type="video/mp4"></video>
<figcaption>Same nudged plate. Left: position control. Right: low stiffness.</figcaption>
</figure>

## Placing

Two millimetres is less than the vision error, so the holder's own ridges do the locating. Land, push into one ridge, push into the other, lift, press down. Every move ends on a force threshold.

<figure class="anim">
<svg viewBox="0 0 1100 440" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Top-down animation: the plate descends onto the holder at an offset, is pushed against the bottom ridge, then the side ridge, lifted and nudged into the corner, then pressed down until it is seated.">
<style>
.pl-t{font-size:18px;fill:#111111}
.pl-h{font-size:19px;font-weight:600;fill:#111111}
.pl-nest{fill:#f1f1f1;stroke:#555555;stroke-width:2}
.pl-ridge{fill:#d2d2d2}
.pl-pocket{fill:none;stroke:#555555;stroke-width:2;stroke-dasharray:8 7}
.pl-plate{fill:#d9d9d9;stroke:#111111;stroke-width:2.5}
.pl-seat{fill:none;stroke:#111111;stroke-width:5}
.pl-fing{fill:#111111}
.pl-shadow{fill:#111111}
.pl-acc{fill:none;stroke:#111111;stroke-width:4;stroke-linecap:round;stroke-linejoin:round}
.pl-dot{fill:#111111}
.pl-ok{font-size:19px;font-weight:600;fill:#111111}
#pl-g{animation:pl-g 12s ease-in-out infinite}
#pl-sh{animation:pl-sh 12s ease-in-out infinite}
#pl-a1{animation:pl-a1 12s linear infinite}
#pl-a2{animation:pl-a2 12s linear infinite}
#pl-seat{animation:pl-late 12s linear infinite}
#pl-ok{animation:pl-late 12s linear infinite}
#pl-dot{animation:pl-dot 12s steps(1) infinite}
@keyframes pl-g{0%,18%{transform:translate(70px,-60px)}32%,36%{transform:translate(70px,0)}50%,60%{transform:translate(0,0)}68%,100%{transform:translate(-2px,2px)}}
@keyframes pl-sh{0%,8%{transform:translate(10px,12px);opacity:.16}18%,54%{transform:translate(2px,2px);opacity:.16}60%,66%{transform:translate(10px,12px);opacity:.16}74%,100%{transform:translate(0,0);opacity:0}}
@keyframes pl-a1{0%,30%{opacity:0}33%,40%{opacity:1}44%,100%{opacity:0}}
@keyframes pl-a2{0%,48%{opacity:0}51%,58%{opacity:1}62%,100%{opacity:0}}
@keyframes pl-late{0%,76%{opacity:0}82%,100%{opacity:1}}
@keyframes pl-dot{0%{transform:translateY(0)}18%{transform:translateY(52px)}36%{transform:translateY(104px)}54%{transform:translateY(156px)}74%{transform:translateY(208px)}}
</style>
<rect class="pl-nest" x="300" y="60" width="340" height="320" rx="10"/>
<rect class="pl-ridge" x="300" y="340" width="340" height="40" rx="6"/>
<rect class="pl-ridge" x="300" y="60" width="40" height="320" rx="6"/>
<rect class="pl-pocket" x="340" y="140" width="240" height="200" rx="6"/>
<g id="pl-g">
<rect id="pl-sh" class="pl-shadow" x="340" y="140" width="240" height="200" rx="6"/>
<rect class="pl-plate" x="340" y="140" width="240" height="200" rx="6"/>
<rect id="pl-seat" class="pl-seat" x="340" y="140" width="240" height="200" rx="6"/>
<rect class="pl-fing" x="334" y="210" width="12" height="60" rx="2"/>
<rect class="pl-fing" x="574" y="210" width="12" height="60" rx="2"/>
</g>
<g id="pl-a1"><path class="pl-acc" d="M530 300 V336 M518 324 L530 338 L542 324"/></g>
<g id="pl-a2"><path class="pl-acc" d="M400 240 H346 M358 228 L344 240 L358 252"/></g>
<text id="pl-ok" class="pl-ok" x="300" y="44">Seated</text>
<text class="pl-h" x="690" y="74">Five moves</text>
<g id="pl-dot"><circle class="pl-dot" cx="676" cy="114" r="6"/></g>
<text class="pl-t" x="690" y="120">Descend until the wrist reads 0.75 N</text>
<text class="pl-t" x="690" y="172">Push to the bottom ridge until 1 N</text>
<text class="pl-t" x="690" y="224">Push to the side ridge until 1 N</text>
<text class="pl-t" x="690" y="276">Lift 5 mm, nudge 3 mm into the corner</text>
<text class="pl-t" x="690" y="328">Press down until 7 N</text>
<text class="pl-t" x="300" y="416">The holder from above. Two ridges locate the plate. Dashed: seated.</text>
</svg>
</figure>

<figure>
<video data-autoplay muted loop playsinline preload="none" poster="/media/lab/place_ridge.jpg"><source src="/media/lab/place_ridge.mp4" type="video/mp4"></video>
<figcaption>The five moves on the robot, from the wrist camera.</figcaption>
</figure>

## Navigation

Nav2 on the base. FAST-LIO2 on an Ouster LiDAR for odometry, ICP against a prior map for localisation.

<figure class="portrait-clip">
<video data-autoplay muted loop playsinline preload="none" poster="/media/lab/nav.jpg"><source src="/media/lab/nav.mp4" type="video/mp4"></video>
</figure>

## What's next

- **Learn the correction from touch.** The robot labels its own data: seat the plate, lift, offset by a known amount, press back down, record the wrench.
- **Fine-tune on the robot with RL**, SERL-style, so a new holder takes a few trials instead of a new geometry.
