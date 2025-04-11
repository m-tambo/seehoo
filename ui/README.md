# Seehoo UI

### Technology
React, React Router, Typescript, Scss, Docker

### Local Development
#### Environment
Setup a `.env` file in the parent directory. A template is provided.
#### Adding Dependencies
Dependencies are handled from within the container. (See overall readme for instructions on spinning up the entire app suite).

- exec into the container: `docker exec -it seehoo-frontend-1 sh`
- use yarn: `yarn add <package>`
