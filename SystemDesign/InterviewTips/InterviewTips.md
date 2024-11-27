
# Gathering System requirements

- **Functional Requirements**: What the system should do. 
  - Gather all 
  - Use the judgement.
  - 


- **Non-Functional Requirements**: How the system should do it.
  - Scale of the design.
  - How many users.
  - Regional users/ Global users.
  - Scale can also be to do with the usage, not just the users. For example google drive has less users but the usage is very high.
  - Latency.
  - Availability -> how many nines.



# Planning

- Write up a plan(1 or 2 mins)
  - Each step is a logical unit that can be handled in isolation
  - This is very important step, also in the coding. Make a structure in mind and then start coding.
  - This can have you know what is in the interviewers mind and they can nudge you there itself if you are going in the wrong direction.
  - 

- Example
  - Design Instagram
    - First start with the storage solution
      - Storing Metadata/profile data(part a)
      - Store images and media(part b)
    
    - Explore page
    - Feed page
    - 
  - Design Ebay
    - Buyer Side
    - Seller Side

# Estimation

- Example:
- System that values the low latency(critical system)
  - Cache Data in api servers so as to avoid to get data from Database everytime
  - is it feasable?
  - How big is the data?
  - How much storage 1 profile picture takes?
  - Does it fit in memory?
  - How many users have these pictures?








## cheatsheet for storage.

- 1 kb = 10^3 bytes 
- 1mb = 10^6 bytes
- 1gb = 10^9 bytes
- 1tb = 10^12 bytes
- 1pb = 10^15 bytes

## Storage Scale Cheatsheet

A character = 1 Byte

Typical metadata for a file/thing = 10 KB
High Quality Image = 2 MB
20 mins HD video = 1 GB


## Storage Capacity cheat sheet

10 TB of disk per machine
256-1TB ram per machine


## Latency Cheat Sheet

How long does it take to have an HTTP request

Intra Continental
50 -150 ms

Cross Continental
200-500 ms

Bandwidth CheatSheet

Mobile Phone
2G - 50-100 kbps
3G - 1-2 Mbps
4G - 10-20 Mbps
5G - 100 Mbps

Broadband
10-100 Mbps

Data Center
1-10 Gbps




# Communication

Convey to the interviewer that you're good at this position.

1. Use System Design Knowledge
2. Communication Skills
   - Being Clear and 
   - unambiguous
   - very Clear and correct intentions
   - Example of bad question: How big is the system? -> ask for number of users/ usage
   - Explain the thought process for your design decision.
   - There could be an alertnative then explain the tradeoffs.
   - Frequently confirm with the interviewer if you are on the right track and get the validation.

# Diagraming

- Annotate the shapes and lines
- Be consistent with shapes
- Make use of the space very well