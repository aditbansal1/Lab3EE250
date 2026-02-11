Question 1: Why are RESTful APIs scalable?

REST keeps requests stateless, uses a uniform interface, and caches, so traffic can be spread across identical servers or layers without coordinating per-client session state.


Question 2: What are the resources the mail server is providing to clients?

The resources are the individual mail entries or messages stored in the system.


Question 3: What is one common REST Method not used in our mail server? How could we extend our mail server to use this method?

A common REST method not used in the current mail server is PUT, could be used to update existing emails.


Question 4: Why are API keys used for many RESTful APIs? What purpose do they serve?

Authentication and Identification: They allow the server to verify that the person making the request is an authorized user 
Rate Limiting: They help providers track how many requests a specific user is making to manage server load.
Security: They act as a basic security layer to ensure that only registered clients can access the resource, which is important for paid APIs


Reference: AWS, "What is a RESTful API?" and Google Cloud API Documentation (2024). https://aws.amazon.com/what-is/restful-api/
