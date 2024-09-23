---
layout: archive
title: 
permalink: /projects/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

Projects
======
* **Leveraging Large Language Models for robotic systems**: May 2023 - Current\
Current robotic systems face a critical limitation in their ability to interact with only a predefined set of objects. Even with the advent of vast and ever-expanding datasets, the system encounters a major challenge when confronted with objects outside this restricted domain. On the other hand, Large Language Models (LLMs) and Vision Language Models (VLMs), meticulously trained on extensive internet-scale data, can provide robots with prior knowledge, enabling them to ground and interact effectively with novel objects. The primary goal of this project is to utilize the zero-shot generalization capabilities of these models to create a holistic robotic system encompassing perception, planning, and lower-level behaviors.

---

* **Task planning under uncertainity for language-guided mobile manipulator** : July 2022 - August 2023\
A robot working as a teammate alongside a human must possess the ability to comprehend natural language instructions given by the user. The robot should be able to perceive the environment around it and generate the sequence of actions to complete the instructed task. Unlike in indoor environments, the uncertainities and dynamism of the outdoor environments make perception and planning for field robots challenging. To this extent, we created the system which monitors the execution of the low-level action and replans in case of any discrepancy between the expected and the perceived state. Furthermore, the partial observability of states in field settings adds to the complexity of the problem. In order to address this issue, our pipeline incorporates exploratory behaviors that are spawned by the planner when it encounters incomplete information, ensuring that a plan can be generated for the intended task. [Video](https://youtu.be/sB60bjTd4go), [Manuscript](https://drive.google.com/file/d/1gtn0kY44iUEqSBu9fpOs9r2zEnOT0c26/view?usp=drive_link)

---

* **Underwater Image Enhancement** : July 2021 - April 2022\
Underwater images are characterized by low contrast, color distortion, and poor visual appearance due to suspended particles' dispersion and scattering of light. We developed a novel fusion-based method that combines the Dark Channel Prior (DCP) and Retinex followed by different image enhancement methods. The color cast effect was removed using our own color balancing algorithms. Neural network methods, UNET and CycleGAN were also implemented to improve the quality of these images. Finally, we concluded the project by incorporating object detection and showed the superiority of our proposed method in the increased accuracy in detecting underwater objects. [Thesis](https://drive.google.com/file/d/1ADiXYufhGzuSJF_GerbJmMzHQ3YGhuF3/view?usp=sharing)

---

* **Modelling, Control and Simulation of Quadruped robots** : April 2021 - September 2021 \
First the simulation was carried out in kinematics level using the closed loop inverse kinematics formulation for the 6D pose control of torso center and 4 foot end effector frames. Then the dynamics modelling was carried out using Composite Rigid body algorithm and Recursive Newton-Euler algorithm. Joint space and task space inverse dynamics control was used to achieve the desired pose regulation of torso and foot frames. The control formulation also took into consideration the different types of constraints (holonomic, nonholonomic due to underactuation and virtual). Simulations were then carried out in MATLAB. Contact Impact Dynamics and compensation for constraint drifts were also modelled for simulation purposes.\
[Video1](https://youtu.be/GAu-791Tc70), [Video2](https://youtu.be/n5TkmluuKZQ), [Report](https://drive.google.com/file/d/1k0NgwT7gTCXW-6YHrqzsvzMsZ65F2Xzy/view?usp=drive_link)

---

* **Brain Tumor classification using ResNet** : January 2021 - April 2021 \
ResNet is a CNN architecture which was designed to enable hundreds of hidden layers to be stacked up without having performance degradation. This is achieved by make use of so-called identity shortcut connections to solve the problem of vanishing gradients. This project focused on the implementation of the architecture on tensorflow and comparison of various performance improving measures. Finally the model was deployed on a medical image dataset containing scan images of brain tumours.

---

* **3-Band Audio Equalizer** : March 2020 - May 2020\
An opamp based Audio Equalizer circuit was designed to individually vary the gain of Bass, Mid, and Treble. The circuit also included several other features such as distortion detection and master gain control. The design was carried out in Matlab and the circuit simulation was done in the Proteus software package.

---

* **Electronic Voting Machine** : January 2020 - February 2020 \
A 8051 micro-controller was used to build an Electronic Voting Machine (EVM) which could be used to vote for two candidates. A 16x2 LCD was incorporated into the design to view the results as well as the status of the election. The design and simulation were done in Proteus.

---

* **Modelling, Control and Simulation of planar robotic manipulator** : May 2019 - July 2020\
Initially, the general mathematical framework for kinematic analysis was studied and the relation between Joint space and Task space velocity kinematics was established in terms of task Jacobian. Then the manipulator dynamics were modelled based on Euler-Lagrange equations of motion. The CAD model of planar manipulator was generated using SolidWorks software package and the mass-inertia properties were extracted. The control design was carried out in both Joint space and Task space. The control design and simulation were carried out using MATLAB/SIMULINK. Finally, the manipulator linkages were analysed for their structural dynamic parameters using ANSYS software to ensure the absence of any control structure interaction. [Report](https://drive.google.com/file/d/1jaEdBx1TYZqzEl0E7jba9-ifKCAvCTJq/view?usp=drive_link)

