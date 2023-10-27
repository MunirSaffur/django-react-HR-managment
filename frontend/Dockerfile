# Use a Node.js base image that includes npm
FROM node:14

# Create and set the working directory
WORKDIR /app

# Copy package.json and package-lock.json files to the container
COPY package*.json ./

# Install Node.js and npm
RUN apt-get update && apt-get install -y nodejs npm

# Install project dependencies
RUN npm install

# Copy the rest of your React app files to the container
COPY . .

# Specify the command to run your React app
CMD [ "npm", "start" ]
