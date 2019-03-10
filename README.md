<h1> Farmbot Techlauncher </h1>

<h2><a name = "content"> Table of Contents </a></h2>
<a href = "#Title1"><b> 1. Project Description </b></a><br/>
<a href = "#Title2"><b> 2. Project Administration </b></a><br/>
<a href = "#Title3"><b> 3. Documentation </b></a><br/>
<a href = "#Title4"><b> 4. Current Progress </b></a><br/>
<a href = "#Title5"><b> 5. Technical Tools and Constraints </b></a>

<br />
<h2><a name = "Title1"> 1. Project Overview </a></h2>

The [Farmbot](https://farm.bot/) is an autonomous agricultural tool which works over a small area to test small-scale agriculture, and has the potential to eventually become a framework for driverless tractors or drones. Current Farmbot software has the capability for simple placement of individual plants, and execute simple commands like watering and fertilizing certain plants. Our expectations of the project is to adopt machine learning skills and modelling techniques to reinforce the capability of Farmbot to automate group plantations and duplicate commands. Our modifications on Farmbot aim to enhance the capability of controlling and monitoring. Our priorities are to optimise plant management and leverage the technology of the Farmbot platform.

<br />
<h2><a name = "Title2"> 2. Project Administration </a></h2>

<h3> 2.1 Timeline </h3>

Week 2-3 Discovery Stage <br />
Week 4-5 Alpha Version - Able to send commands to Farmbot <br />
Week 6-9 Beta Version - Most commands have been implemented in code, which compiles and is received by Farmbot. Data is able to be input  through CSV or text files <br />
Week 10-12 Reflection and Improvements <br />

<h3> 2.2 Deliverables </h3>

* Modular Python code that implements:
    * New version of Farm Design, which accepts CSV files as a way of defining groups of plants, and also keeps some of the original functionality such as telling you when plants are too closely spaced together, and displaying information on the plants.
    * New version of the existing sequences, which are associated with Farm Design groups, supports loops, accepts JSON, yaml, or text files as ways of defining these tasks, and has the option to output logs in both CSV and custom text format
    * New text-based implementation of Regimens, which are associated with Farm Design groups.
    * New text-based implementation of Farm Events, which are associated with Farm Design groups.
    * Some way to test commands without ruining the garden bed.
    * All implementations should also be able to create, edit and write to files that store these Farm Designs, Sequences, Regimens, and Events, and have their callable functions structured in a way that would easily support the future addition of a GUI.
    
* Documentation:
    * High level documentation of the code, to be done as we go in a wiki format on GitHub
    * Well commented code
    * Commit messages should be a good description of changes made in that commit. If you want to make many changes, please do it in separate commits.
    * A guide on how to use the resulting code, to be handed to the stakeholders and made available on GitHub

<h3> 2.3 Traceability of Actions </h3>
We are using Github issues and project wiki to track actions and deliverables.

<h3> 2.4 Team </h3>

| Team Member                      | Role                                     | Email                           | 
|----------------------------------|------------------------------------------|---------------------------------|  
| Member 1                         | Role                                     | uXXXXXXX@anu.edu.au             |
| Member 2                         | Role                                     | u5807060@anu.edu.au             | 
| Maojun Zhu                       | Role                                     | u6170753@anu.edu.au             |
| Member 4                         | Role                                     | uXXXXXXX@anu.edu.au             |
| Member 5                         | Role                                     | uXXXXXXX@anu.edu.au             |
| Member 6                         | Role                                     | uXXXXXXX@anu.edu.au             |
| Wenjing Gu                       | Member                                   | u6203160@anu.edu.au             |

<h3> 2.5 Stakeholders </h3>

Ming-Dao Chia is our client and main point of contact. We meet with Ming weekly and communicate regularly on Slack. 
Our team works on software and collaborate with students from Engineering to discover and optimize the functionalities of Farmbot platform.

<br />
<h2><a name = "Title3"> 3. Support Documentation </a></h2>

**Statement of Work**

>Link to Statement of Work <br />

**Team Communication**

>Link to Slack <br />
>Link to Client/Team meetings, how often <br />

**Team Progress Tracking**

>Link to Github issues <br />
>Link to Weekly Log <br />

**Legal Documents**

Not required

<br />
<h2><a name = "Title4"> 4. Current Progress </a></h2>

Current Progress: Completed github landing page, established roles and started discovery

<h2>Milestones:</h2> 
<br/>
Phase 1: Discovery Report to demonstrate project specifications and requirements <br/>
Phase 2: Record observations and testings to list down the functionality of Alpha version <br/>
Phase 3: Implement the Beta version to task on the project Requirements<br/>
Phase 4: Testings and Feedbacks to Beta Version<br/>
Phase 5: Improvements on Beta Version and Demonstration of functionality of project<br/>


<br />
<h2><a name = "Title5"> 5. Technical Tools and Constraints</a></h2>

* Available Tools:
    * One FarmBot XL for testing
    * Existing code base, particularly the RESTful API, which means it can work with modules written in other languages (originally written in Ruby)
* Constraints:
    * Some testing has to be done on site with physical machines
    * Python is the preferred language

