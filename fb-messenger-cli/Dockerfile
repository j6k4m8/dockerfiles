FROM kinlan/puppets:latest


# Run everything after as non-privileged user.
RUN apt -y update 
RUN apt -y install git
RUN git clone --depth 1 https://github.com/Alex-Rose/fb-messenger-cli.git app
WORKDIR app 
RUN npm i puppeteer
RUN groupadd -r pptruser && useradd -r -g pptruser -G audio,video pptruser
USER pptruser
CMD ["bash", "-c", "google-chrome-unstable --no-sandbox && fb-messenger-cli"]
#CMD ["node", "cli.js"]
