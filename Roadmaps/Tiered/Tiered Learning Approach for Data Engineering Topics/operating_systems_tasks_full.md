# Operating Systems: OSTEP & Berkeley CS 162 - Detailed Task Breakdown (90 Blocks)

This document will outline 90 specific study blocks for "Operating Systems," based on "Operating Systems: Three Easy Pieces" (OSTEP) by Remzi H. Arpaci-Dusseau and Andrea C. Arpaci-Dusseau, and relevant Berkeley CS 162 lectures. Each block is designed for approximately 50 minutes of focused study.

**Resource Key:**
*   **OSTEP:** *Operating Systems: Three Easy Pieces* (Arpaci-Dusseau) - Online at pages.cs.wisc.edu/~remzi/OSTEP/
*   **CS 162 Lect:** UC Berkeley CS 162 Lectures (e.g., Fall 2021 Playlist by John Kubiatowicz or similar recent series).
*   **HW/Lab:** Homework, lab exercises, or thought experiments related to OSTEP chapters or CS 162 concepts.

---

**Part I: Virtualization**

**Module 1: Introduction to Operating Systems (OSTEP Chapters 1-3) (Approx. 5 Blocks)**

*   **Block 1 (Task 1/90): What is an OS? Dialogue & History**
    *   OSTEP: A Dialogue on Operating Systems (Intro chapter), Chapter 1 (A Brief History of Operating Systems)
    *   CS 162 Lect 1: What is an Operating System?
*   **Block 2 (Task 2/90): Introduction to Operating Systems Concepts**
    *   OSTEP: Chapter 2 (Introduction to Operating Systems)
    *   CS 162 Lect 2: Four Fundamental OS Concepts (or similar overview lecture).
*   **Block 3 (Task 3/90): The Abstraction: The Process**
    *   OSTEP: Chapter 3 (Dialogue: The CRUX of the Matter), Chapter 4 (The Abstraction: The Process)
    *   CS 162 Lect 3: Abstractions 1: Threads and Processes (focus on Process part).
*   **Block 4 (Task 4/90): Process API**
    *   OSTEP: Chapter 5 (Interlude: Process API - fork, exec, wait)
    *   HW: Simple C programs using fork, exec, wait.
*   **Block 5 (Task 5/90): Direct Execution & CPU Virtualization**
    *   OSTEP: Chapter 6 (Mechanism: Limited Direct Execution)
    *   CS 162 Lect (relevant segment on CPU virtualization challenges).

**Module 2: CPU Scheduling (OSTEP Chapters 7-10) (Approx. 10 Blocks)**

*   **Block 6 (Task 6/90): Scheduling Introduction & Metrics**
    *   OSTEP: Chapter 7 (Scheduling: Introduction - Workload Assumptions, Metrics)
    *   CS 162 Lect 5: Scheduling Algorithms I (Intro, FIFO, SJF, STCF).
*   **Block 7 (Task 7/90): FIFO, SJF, STCF**
    *   OSTEP: Chapter 7 (FIFO, SJF, STCF examples and analysis)
    *   HW: Calculate turnaround/response for given job sets with these algorithms.
*   **Block 8 (Task 8/90): Round Robin Scheduling**
    *   OSTEP: Chapter 7 (Round Robin)
    *   CS 162 Lect (segment on Round Robin).
*   **Block 9 (Task 9/90): Incorporating I/O**
    *   OSTEP: Chapter 7 (Incorporating I/O)
*   **Block 10 (Task 10/90): Multi-Level Feedback Queue (MLFQ)**
    *   OSTEP: Chapter 8 (Scheduling: The Multi-Level Feedback Queue)
    *   CS 162 Lect 6: Scheduling Algorithms II (MLFQ).
*   **Block 11 (Task 11/90): MLFQ Rules & Examples**
    *   OSTEP: Chapter 8 (MLFQ Rules, Examples, Tuning)
    *   HW: Trace job execution through an MLFQ.
*   **Block 12 (Task 12/90): Proportional Share (Lottery Scheduling)**
    *   OSTEP: Chapter 9 (Scheduling: Proportional Share - Lottery Scheduling)
*   **Block 13 (Task 13/90): Lottery Scheduling Implementation & Stride Scheduling**
    *   OSTEP: Chapter 9 (Lottery Tickets, Stride Scheduling)
    *   CS 162 Lect (if Lottery/Stride scheduling is covered).
*   **Block 14 (Task 14/90): Multiprocessor Scheduling**
    *   OSTEP: Chapter 10 (Multiprocessor Scheduling (Advanced))
    *   CS 162 Lect (segment on multiprocessor scheduling challenges).
*   **Block 15 (Task 15/90): Scheduling Review & Problem Solving**
    *   Review OSTEP Chapters 7-10.
    *   Work through OSTEP homework problems for scheduling.

**Module 3: Memory Virtualization (Address Spaces) (OSTEP Chapters 13-17) (Approx. 12 Blocks)**

*   **Block 16 (Task 16/90): Address Spaces Introduction**
    *   OSTEP: Chapter 13 (Dialogue: The CRUX of Memory), Chapter 14 (The Abstraction: Address Spaces)
    *   CS 162 Lect 7: Address Spaces.
*   **Block 17 (Task 17/90): Memory API & Address Translation Intro**
    *   OSTEP: Chapter 15 (Interlude: Memory API - malloc, free)
    *   OSTEP: Chapter 16 (Mechanism: Address Translation - Assumptions, Examples)
*   **Block 18 (Task 18/90): Base and Bounds (Dynamic Relocation)**
    *   OSTEP: Chapter 16 (Base and Bounds, Hardware Support, OS Issues)
    *   CS 162 Lect (segment on base & bounds).
*   **Block 19 (Task 19/90): Segmentation**
    *   OSTEP: Chapter 17 (Mechanism: Segmentation - Generalized Base/Bounds, Which Segment?)
*   **Block 20 (Task 20/90): Segmentation Support & Fine-grained vs Coarse-grained**
    *   OSTEP: Chapter 17 (Fine-grained vs. Coarse-grained Segmentation, OS Support)
    *   HW: Compare segmentation with base/bounds for different scenarios.
*   **Block 21 (Task 21/90): Free-Space Management**
    *   OSTEP: Chapter 18 (Mechanism: Free-Space Management - Assumptions, Strategies: Best/Worst/First Fit)
    *   CS 162 Lect 8: Memory Allocation I (Free Space Management).
*   **Block 22 (Task 22/90): Buddy System & Other Approaches**
    *   OSTEP: Chapter 18 (Buddy System, Other Approaches)
    *   HW: Implement a simple free-space allocator.
*   **Block 23 (Task 23/90): Paging: Introduction**
    *   OSTEP: Chapter 19 (Mechanism: Paging - A First Look, Page Table, Array of Pointers)
    *   CS 162 Lect 9: Paging & TLBs I.
*   **Block 24 (Task 24/90): Paging: Page Table Structure & Size**
    *   OSTEP: Chapter 19 (Where are Page Tables Stored?, What is in the Page Table Entry?, Paging is Slow)
*   **Block 25 (Task 25/90): Paging: TLBs (Translation Lookaside Buffers)**
    *   OSTEP: Chapter 20 (Mechanism: Paging - Translation Lookaside Buffers (TLBs))
    *   CS 162 Lect 9: Paging & TLBs I (TLB part).
*   **Block 26 (Task 26/90): TLB Issues: Context Switch, Replacement Policy**
    *   OSTEP: Chapter 20 (Who Handles a TLB Miss?, TLB Contents, TLB Issue: Context Switch, TLB Issue: Replacement Policy)
*   **Block 27 (Task 27/90): Advanced Page Tables: Larger Page Tables**
    *   OSTEP: Chapter 21 (Mechanism: Paging - Smaller Tables - Hybrid Approach, Multi-level Page Tables)
    *   CS 162 Lect 10: Paging & TLBs II (Multi-level Page Tables).

**Module 4: Swapping & Page Replacement (OSTEP Chapters 22-24) (Approx. 10 Blocks)**

*   **Block 28 (Task 28/90): Swapping: Mechanisms**
    *   OSTEP: Chapter 22 (Mechanism: Swapping - Memory Overload, Swap Space, The Present Bit)
    *   CS 162 Lect 11: Demand Paging & Swapping.
*   **Block 29 (Task 29/90): Page Faults & Page Replacement Basics**
    *   OSTEP: Chapter 22 (The Page Fault, Page Replacement, When to Evict?)
*   **Block 30 (Task 30/90): Page Replacement Algorithms: FIFO, Random**
    *   OSTEP: Chapter 23 (Policy: Page Replacement - Optimal, FIFO, Random)
    *   HW: Trace page faults for FIFO/Random with a reference string.
*   **Block 31 (Task 31/90): Page Replacement: LRU, Clock**
    *   OSTEP: Chapter 23 (Using History: LRU, Approximating LRU - Clock Algorithm)
    *   CS 162 Lect 12: Page Replacement Algorithms (LRU, Clock).
*   **Block 32 (Task 32/90): Clock Algorithm Variants & Other Policies**
    *   OSTEP: Chapter 23 (Considering Dirty Pages, Other Page Replacement Policies)
*   **Block 33 (Task 33/90): Thrashing & Working Set Model**
    *   OSTEP: Chapter 24 (Policy: Swapping - Thrashing, Working Set Model)
*   **Block 34 (Task 34/90): Page Fault Control & Other Swapping Policies**
    *   OSTEP: Chapter 24 (Page Fault Frequency, Other Swapping Policies)
*   **Block 35 (Task 35/90): Memory Virtualization Review Session 1**
    *   Review OSTEP Chapters 13-21 (Address Spaces, Translation, Paging, TLBs).
    *   Work through OSTEP homework problems.
*   **Block 36 (Task 36/90): Memory Virtualization Review Session 2**
    *   Review OSTEP Chapters 22-24 (Swapping, Page Replacement).
    *   Work through OSTEP homework problems.
*   **Block 37 (Task 37/90): Case Study: The VAX/VMS Virtual Memory System (Optional/Skim)**
    *   OSTEP: Chapter 25 (Case Study: The VAX/VMS Virtual Memory System)

**Part II: Concurrency**

**Module 5: Concurrency & Threads (OSTEP Chapters 26-28) (Approx. 8 Blocks)**

*   **Block 38 (Task 38/90): Introduction to Concurrency**
    *   OSTEP: Chapter 26 (Dialogue: The CRUX of Concurrency), Chapter 27 (Concurrency: An Introduction - Threads, Shared Data)
    *   CS 162 Lect 13: Concurrency & Threads I.
*   **Block 39 (Task 39/90): Thread API & Race Conditions**
    *   OSTEP: Chapter 27 (Thread API - Create, Join, Mutexes, Condition Variables), Chapter 28 (Interlude: Thread API - Example: Race Condition)
*   **Block 40 (Task 40/90): Locks: Introduction & Building Locks**
    *   OSTEP: Chapter 29 (Mechanism: Locks - The Basic Idea, Building A Lock - Test-And-Set, Compare-And-Swap)
    *   CS 162 Lect 14: Synchronization I (Locks, Semaphores).
*   **Block 41 (Task 41/90): Spin Locks & Other Lock Optimizations**
    *   OSTEP: Chapter 29 (Evaluating Locks, Spin Locks with Test-and-Set, Other Spin Lock Optimizations)
*   **Block 42 (Task 42/90): Locks: Avoiding Spin, Different OS Support**
    *   OSTEP: Chapter 29 (Just Say No To Spin: Using Queues, Different OS Support)
*   **Block 43 (Task 43/90): Locked Data Structures**
    *   OSTEP: Chapter 30 (Policy: Locked Data Structures - Concurrent Counters, Concurrent Linked Lists, Concurrent Queues, Concurrent Hash Tables)
*   **Block 44 (Task 44/90): Condition Variables**
    *   OSTEP: Chapter 31 (Mechanism: Condition Variables - Definition and Routines, Producer/Consumer Problem)
    *   CS 162 Lect 15: Synchronization II (Condition Variables, Monitors).
*   **Block 45 (Task 45/90): Semaphores**
    *   OSTEP: Chapter 32 (Mechanism: Semaphores - Definition, Binary Semaphores (Locks), Semaphores For Ordering, The Producer/Consumer Problem)
    *   HW: Solve classic synchronization problems using semaphores.

**Module 6: Concurrency Problems & Event-based Concurrency (OSTEP Chapters 33-34) (Approx. 7 Blocks)**

*   **Block 46 (Task 46/90): Common Concurrency Problems (Bugs)**
    *   OSTEP: Chapter 33 (Policy: Common Concurrency Problems - Non-Deadlock Bugs: Atomicity Violation, Order Violation)
*   **Block 47 (Task 47/90): Deadlock: Conditions & Prevention**
    *   OSTEP: Chapter 33 (Deadlock Bugs: Conditions for Deadlock, Prevention - Circular Wait, Hold-and-Wait, No Preemption, Mutual Exclusion)
    *   CS 162 Lect 16: Deadlock.
*   **Block 48 (Task 48/90): Deadlock: Avoidance & Detection/Recovery**
    *   OSTEP: Chapter 33 (Deadlock Avoidance via Scheduling, Detection and Recovery)
*   **Block 49 (Task 49/90): Event-based Concurrency (Non-blocking I/O)**
    *   OSTEP: Chapter 34 (Mechanism: Event-based Concurrency (Advanced) - The Basic Idea: An Event Loop, An Important API: select() or poll())
*   **Block 50 (Task 50/90): Difficulties with Event-based Concurrency**
    *   OSTEP: Chapter 34 (Why Simpler? Difficulties, Combining Events and Threads)
*   **Block 51 (Task 51/90): Concurrency Review Session 1**
    *   Review OSTEP Chapters 26-32 (Threads, Locks, CVs, Semaphores).
    *   Work through OSTEP homework problems.
*   **Block 52 (Task 52/90): Concurrency Review Session 2**
    *   Review OSTEP Chapters 33-34 (Concurrency Bugs, Deadlock, Event-based).
    *   Work through OSTEP homework problems.

**Part III: Persistence**

**Module 7: I/O Devices & Disks (OSTEP Chapters 36-38) (Approx. 8 Blocks)**

*   **Block 53 (Task 53/90): I/O Devices Introduction**
    *   OSTEP: Chapter 36 (Dialogue: The CRUX of Persistence), Chapter 37 (I/O Devices - System Architecture, A Canonical Device, The OS And I/O)
    *   CS 162 Lect 17: I/O Devices & Disks.
*   **Block 54 (Task 54/90): Hard Disk Drives: Mechanics & Performance**
    *   OSTEP: Chapter 38 (Mechanism: Hard Disk Drives - The Interface, Basic Geometry, A Simple Disk Drive, Disk Performance)
*   **Block 55 (Task 55/90): Disk Scheduling**
    *   OSTEP: Chapter 38 (Disk Scheduling: SSTF, SCAN/Elevator, C-SCAN)
*   **Block 56 (Task 56/90): RAID: Introduction & Levels 0, 1**
    *   OSTEP: Chapter 39 (Mechanism: Redundant Arrays of Inexpensive Disks (RAIDs) - Interface, Fault Model, RAID Level 0, RAID Level 1)
    *   CS 162 Lect 18: Filesystems I (RAID, Intro to FS).
*   **Block 57 (Task 57/90): RAID Levels 4, 5**
    *   OSTEP: Chapter 39 (RAID Level 4, RAID Level 5)
*   **Block 58 (Task 58/90): Other RAID Levels & Issues**
    *   OSTEP: Chapter 39 (Other RAID Issues, A Final Note On RAID)
*   **Block 59 (Task 59/90): Interlude: Files and Directories**
    *   OSTEP: Chapter 40 (Interlude: Files and Directories - Files, Directories, File System API)
*   **Block 60 (Task 60/90): File System Implementation: Overview & Data Structures**
    *   OSTEP: Chapter 41 (Mechanism: File System Implementation - Thinking About The Problem, Overall Organization, On-Disk File System Structure)
    *   CS 162 Lect 19: Filesystems II (FAT, FFS).

**Module 8: File Systems (OSTEP Chapters 41-44) (Approx. 15 Blocks)**

*   **Block 61 (Task 61/90): File System Implementation: Access Paths & Caching**
    *   OSTEP: Chapter 41 (Access Paths: Reading and Writing, Caching and Buffering)
*   **Block 62 (Task 62/90): Locality and The Fast File System (FFS)**
    *   OSTEP: Chapter 42 (Policy: Locality and The Fast File System - The Old UNIX File System, The Fast File System (FFS))
*   **Block 63 (Task 63/90): FFS Cylinder Groups & Other Features**
    *   OSTEP: Chapter 42 (FFS: Cylinder Groups, Other FFS Features)
*   **Block 64 (Task 64/90): Crash Consistency: FSCK & Journaling Intro**
    *   OSTEP: Chapter 43 (Mechanism: Crash Consistency - A New CRUX: The Problem of Crashing, Solution #1: The File System Checker (fsck), Solution #2: Journaling (or Write-Ahead Logging))
    *   CS 162 Lect 20: Filesystems III (Journaling, LFS).
*   **Block 65 (Task 65/90): Journaling Implementation Details**
    *   OSTEP: Chapter 43 (Journaling: Data Journaling, Metadata Journaling, Ordering Writes)
*   **Block 66 (Task 66/90): Log-structured File System (LFS)**
    *   OSTEP: Chapter 44 (Policy: Log-structured File System (LFS) - Writing To Disk Sequentially, Cleaning The Log)
*   **Block 67 (Task 67/90): LFS Crash Recovery & Other Issues**
    *   OSTEP: Chapter 44 (LFS: Crash Recovery, Other Issues)
*   **Block 68 (Task 68/90): Data Integrity and Protection**
    *   OSTEP: Chapter 45 (Mechanism: Data Integrity and Protection (Advanced) - Disk Failure Modes, Handling Latent Sector Errors, Detecting Corrupted Data)
*   **Block 69 (Task 69/90): Flash-based SSDs: Introduction & Performance**
    *   OSTEP: Chapter 46 (Mechanism: Flash-based SSDs (Advanced) - Basic Flash Organization, Flash Performance)
    *   CS 162 Lect (if SSDs are covered in detail).
*   **Block 70 (Task 70/90): SSDs: FTL & Wear Leveling**
    *   OSTEP: Chapter 46 (Flash Translation Layer (FTL), Wear Leveling, Other SSD Issues)
*   **Block 71 (Task 71/90): Distributed Systems: Introduction & RPCs**
    *   OSTEP: Chapter 47 (Distributed Systems (Advanced) - Communication Basics, Remote Procedure Call (RPC))
    *   CS 162 Lect 21: Distributed Systems I (RPCs, NFS).
*   **Block 72 (Task 72/90): Distributed File Systems (NFS)**
    *   OSTEP: Chapter 48 (Distributed File Systems (Advanced) - Network File System (NFS), NFSv2, NFSv3, NFSv4)
*   **Block 73 (Task 73/90): Andrew File System (AFS)**
    *   OSTEP: Chapter 48 (The Andrew File System (AFS))
*   **Block 74 (Task 74/90): Persistence Review Session 1**
    *   Review OSTEP Chapters 36-41 (I/O, Disks, RAID, FS Intro).
    *   Work through OSTEP homework problems.
*   **Block 75 (Task 75/90): Persistence Review Session 2**
    *   Review OSTEP Chapters 42-48 (FFS, Journaling, LFS, Distributed FS).
    *   Work through OSTEP homework problems.

**Module 9: Security (OSTEP Chapters 49-50) (Approx. 5 Blocks)**

*   **Block 76 (Task 76/90): Introduction to Security & Principles**
    *   OSTEP: Chapter 49 (Security: An Introduction - Principles of Security, Authentication)
    *   CS 162 Lect 22: Security I (Principles, Threats, Access Control).
*   **Block 77 (Task 77/90): Authorization & Access Control Lists**
    *   OSTEP: Chapter 49 (Authorization: Who Can Access What?, Access Control Lists (ACLs))
*   **Block 78 (Task 78/90): Capabilities & Multi-level Security**
    *   OSTEP: Chapter 49 (Capabilities, Multi-level Security (MLS))
*   **Block 79 (Task 79/90): Cryptography Basics: Symmetric & Asymmetric Encryption**
    *   OSTEP: Chapter 50 (Security: Cryptography - Symmetric Encryption, Asymmetric Encryption)
    *   CS 162 Lect 23: Security II (Crypto, Network Security).
*   **Block 80 (Task 80/90): Hashing, Digital Signatures & Certificates**
    *   OSTEP: Chapter 50 (Cryptographic Hashing, Digital Signatures, Certificates)

**Module 10: Advanced Topics & Review (Approx. 10 Blocks)**

*   **Block 81 (Task 81/90): Case Study: Linux (Selected Topics)**
    *   OSTEP: Chapter 51 (Case Study: The Linux Operating System - History, Design Goals, Processes, Scheduling, Memory Management)
    *   Focus on relating Linux specifics to general OSTEP concepts.
*   **Block 82 (Task 82/90): Linux File System & I/O**
    *   OSTEP: Chapter 51 (Linux File System, I/O, Networking, Security)
*   **Block 83 (Task 83/90): Virtual Machines (Intro & Benefits)**
    *   CS 162 Lect (if VMs are covered, e.g., Lect 24: Virtual Machines).
    *   Read relevant online articles/documentation on VM concepts.
*   **Block 84 (Task 84/90): VM Implementation Techniques (Trap-and-Emulate, Binary Translation)**
    *   CS 162 Lect (VM implementation details).
*   **Block 85 (Task 85/90): Cloud Computing Concepts (IaaS, PaaS, SaaS)**
    *   CS 162 Lect (if Cloud Computing is covered, e.g., Lect 25: Cloud Computing).
    *   Read relevant online articles/documentation.
*   **Block 86 (Task 86/90): OS Review: Virtualization (CPU & Memory)**
    *   Comprehensive review of OSTEP Part I concepts and CS 162 lectures on virtualization.
*   **Block 87 (Task 87/90): OS Review: Concurrency**
    *   Comprehensive review of OSTEP Part II concepts and CS 162 lectures on concurrency.
*   **Block 88 (Task 88/90): OS Review: Persistence**
    *   Comprehensive review of OSTEP Part III concepts and CS 162 lectures on persistence.
*   **Block 89 (Task 89/90): OS Review: Security & Advanced Topics**
    *   Review Security concepts and any advanced topics covered (VMs, Cloud).
*   **Block 90 (Task 90/90): Final OS Problem Solving / Mock Exam Questions**
    *   Work through comprehensive OS problems or past exam questions if available from CS 162.

---

*(Note: This breakdown aims to cover the breadth of OSTEP and align with a typical university OS course like CS 162. The depth of coverage for some "Advanced" OSTEP chapters or specific CS 162 lecture topics might be adjusted to fit the 90-block (75-hour) allocation. Emphasis should be on understanding the core principles and their practical implications for data engineering, such as I/O performance, memory management for large datasets, and concurrency control.)*
