# Base image
FROM node:18

# Set working directory
WORKDIR /app

# Copy package files and install dependencies
COPY package.json yarn.lock ./
RUN yarn install

# Copy the rest of the code
COPY . .

# Set environment variable to control mode (can be overridden at runtime)
ARG NODE_ENV=production
ENV NODE_ENV=${NODE_ENV}

# For dev mode: expose 3000, for prod mode: expose 80 (nginx)
EXPOSE 3000

# If NODE_ENV=development, run yarn start (dev server with hot reload)
# Else, build and serve via nginx
RUN if [ "$NODE_ENV" = "production" ]; then yarn build; fi

CMD [ "sh", "-c", "if [ \"$NODE_ENV\" = \"development\" ]; then yarn start; else npx serve -s build -l 3000; fi" ]
