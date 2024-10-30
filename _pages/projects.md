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

* **Dynamic Gesture based Robot Instruction Following** : Auguest 2024 - Present\
Gestures serve as a vital form of human communication. This project focuses on grounding and interpreting dynamic human gestures, allowing a robot to carry out multi-step actions based on these cues. This advancement not only enhances natural human-robot interaction but also holds promise for supporting communication and interaction between deaf and mute individuals and robots. [Video 1](https://drive.google.com/file/d/1RuwKnAWcDOtyUuaKjDw7FZqyJQx0WyZZ/view?usp=drive_link), [Video 2](https://drive.google.com/file/d/184z7Mr4p2TNtTt8pWQW2zGzoQGr7sKqh/view?usp=drive_link)

* **Advancing Zero-Shot and Robust Robotic Task Planning and Execution in Novel Scenarios** : June 2023 - Present\
An assistive robot working alongside a human must possess the ability to comprehend natural language instructions given by the user. The robot should be able to perceive the environment around it and generate the sequence of actions to complete the instructed task. In real world scenarios, the robot can be in any novel setting. The uncertainities and dynamism of the novel scenarios makes generalization of perception and planning challenging. To this extent, we created the system which interprets human instructions in natural language, generates a task plan based on the current world state and the instruction using a LLM planner, and sequentially executes the plan using a motion planner and a set of skills (pick, place, give, remove, unstack, open, close, etc.). The world state is created and updated regularly using a scene graph generation method developed by us. An action validation mechanism is implemented to provide feedback to the planner after each action, allowing for error recovery in case of failure. [Video](https://drive.google.com/file/d/1Qpc4blP0bpEBzy3m2TczPmLotGx562kW/view?usp=sharing)

---

* **Zero-Shot Spatial Reasoning for Complex Natural Language Instructions Using Foundation Models and Lingo Space Integration** : February 2023 - Present\
Traditional robotic natural-language grounding methods focus on identifying objects and actions, but they often struggle with complex spatial relations in human instructions. For instance, executing commands like *"place the banana to the right of the rectangular basket"* or *"put the spectacles inside the less occupied tray"* requires the robot not only to understand spatial relationships but also to reason over contextual factors like shape, size, color, and occupancy. Existing methods are limited by predefined sets of spatial relations and often fail to handle these intricate instructions because they cannot reason over such predicates. To overcome these limitations, we developed a pipeline that leverages foundation models to generate coarse spatial regions through zero-shot space grounding. This approach enables robots to interpret and execute more complex spatial instructions. In collaboration with KAIST, we integrated their space-grounding method (Lingo Space) to refine these regions. 

---

* **Generalized Grounded Temporal Reasoning for Robot Instruction Following** : January 2024 - September 2024\
Imagine a scenario where a human instructs a robot, “Remove the cloth using which I wiped the table.” This task requires the robot to engage in temporal reasoning by identifying the relevant past interaction, grounding the object in the current scene, and then executing the task. The complexity arises from the multi-step references to past events and the extensive range of possible object groundings in a video stream. To tackle this, we developed a method that decomposes the task into estimating the relevant video segment, performing spatial reasoning to pinpoint the intended object, and tracking its location until the present moment. Our approach leverages large pre-trained models with strong generalization abilities for temporal grounding tasks. [Video](https://drive.google.com/file/d/1F2ubRNycmtKAeMzmsgW1nW0HQ-DSoTvT/view?usp=sharing)

---

* **Open-World Scene Graphs for Human-instructed Manipulation Tasks Using Foundation Models**: November 2023 - May 2024\
To generate effective multi-step plans in robotics, it's essential to have a scene representation that is open-set and structured to allow for easy updates when the scene changes. We introduce a method for creating multi-hierarchical scene graphs in a zero-shot manner using foundation models, which can enhance downstream planning tasks. Our approach demonstrates superior performance compared to previous methods in both open-world object detection and relation extraction, even without prior information. Additionally, we show how the multi-hierarchical structure of the scene graph helps planners develop viable plans for tasks that require reasoning about spatial arrangements and object category abstractions. [Video](https://drive.google.com/file/d/1fZyQ6rZPRxQ3TaKJoGzLJ6W6-iH9NBBr/view?usp=drive_link)

---

* **Dynamic Analysis of Elliptical Trammel Mechanism, Static Analysis of Three Wheeled Robot with Actuator Optimization and Motor Testing** : January 2023 - May 2023 \
The project involved addressing key challenges in robot design, starting with dynamic analysis of elliptical trammel mechanism to raise a wheel in a four-wheeled robot with triangular linkage. Next, the dynamics of a three-wheeled robot were analyzed, focusing on the effects of dead weight on deceleration, circular motion, and curb climbing, resulting in optimal weight placement. Finally, a systematic approach was taken to evaluate and select the best motor type for the robot, considering various options like spur and planetary geared motors. [Thesis](https://drive.google.com/file/d/1jlBRgy4-P4w2H6FxWu7qsI-yx2uFlZyW/view?usp=sharing)

---

* **6DOF Robotic Manipulator Design for Mars Rover** : January 2022 - January 2023 \
One of the founding members of the Consortium for Research in Space Systems (CRISS Robotics), a technical team at BITS Pilani. We actively participated in events such as the International Rover Challenge (IRC) and University Rover Challenge (URC). I was invloved in the development a teleoperated robotic arm manipulator with six degrees of freedom (6DOF). The robotic arm had a payload capacity of 6 kilograms and demonstrated proficiency in executing diverse manipulation tasks. [Website](https://www.criss-robotics.in/)