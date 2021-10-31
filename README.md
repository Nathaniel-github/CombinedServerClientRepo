<div id="top"></div>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://raw.githubusercontent.com/Nathaniel-github/CombinedServerClientRepo/main/TrieServer/imgs/trie.png">
    <img src="https://raw.githubusercontent.com/Nathaniel-github/CombinedServerClientRepo/main/TrieServer/imgs/trie.png" alt="Logo" width="200" height="200">
  </a>

<h3 align="center">Trie Project</h3>

  <p align="center">
    The server code for my globally hosted trie through GCP
    <br />
    <a href="https://trieserver.readthedocs.io/en/latest/index.html"><strong>Explore the server docs »</strong></a> - <a href="https://trieclient.readthedocs.io/en/latest/index.html"><strong>Explore the client docs »</strong></a>
    <br />
    <br />
    <a href="https://pypi.org/project/trie-nathaniel/">View on PyPi</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#thinking">Thinking</a></li>
    <li><a href="#implementation">Implementation</a></li>
    <li><a href="#server-hosting">Server Hosting</a></li>
    <li><a href="#client-interaction">Client Interaction</a></li>
    <li><a href="#documentation">Documentation</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>


<!-- THINKING -->
## Thinking

There were many portions of this project that were pretty unclear in how they should be solved so I did my best to accommodate what I assumed was being looked for with what is the best practice of implementation. The first portion that I just assumed was a given was whether or not this trie had to be a direct implementation by me. Python has a near-infinite number of libraries and one of them is most likely something that would implement a trie but I am just going to go with common sense and say that I shouldn’t be using someone else’s implementation of this data structure. The next portion that was unclear was what exactly ‘display the trie’ meant. Given how this project was given as a CLI and we were given a week to complete it I again just assumed this meant I should just print all the words that existed in the trie and not try to render a graphical representation of it. Lastly, along with that came the issue of how to display it. It doesn’t make sense to iterate through the trie to just get all the words in it if you are given each word as it comes in. The most algorithmically efficient approach would be to just store the words separately and return them on request to display the trie. Since this also might defeat some testing purposes in terms of implementation I decided to offer both options with ‘Display trie’ and ‘Display trie fast’.

<!-- IMPLEMENTATION -->
## Implementation

I made my distribution through PyPi and developed my project using python. I know it is a very slow language I have almost 0 experience using javascript (actually scratch that I don’t know javascript) so it was my best option in terms of creating a CLI and distributing it in a clean way. This is my first time making a project like this as I had no experience with releasing packages through any installation software up until last week. It has been a huge learning journey as I figured out the ins and outs of distributing software on PyPi and hosting documentation using <a href="readthedocs.org">readthedocs.org</a>. On the client-side of implementation, I used a combination of <a href="https://click.palletsprojects.com/en/8.0.x/">click</a> and <a href="https://github.com/magmax/python-inquirer">inquirer</a> to develop the CLI. Click provided a way to take command-line arguments in a neat way and inquirer allowed me to provide a clean UI for users that would rather interact with the trie in a simpler way. On the server side, the connection between the GCP server and clients was made using sockets. I actually have no idea if this is the best way to establish a connection between client and server in a CLI since I have never made one before but from my experience with general networking in game development sockets are usually a good way to go and I have the most experience working with them so it will be easier for me to develop the idea into code. It probably wasn’t necessary but in the off chance that someone sent some huge essay to store in the trie, I did have the server read buffers in increments so that there aren’t the limitations of a fixed buffer in the socket. On the server’s side, I also added a few more features in order to handle off-cases to the best of my knowledge. I started with try excepts to prevent the server from crashing on some error and decided to also send the error to the client so that they wouldn’t end up stalled by the readbuffer that would be attempted after sending their packet. The try excepts were most likely not set up in the most professional way but error handling in python isn’t my Ph.D. so I did the best I could with what I knew. The next thing I thought of that could go wrong is that after all my attempts to prevent the server from going offline it somehow manages to do just that either because of a mess up on GCP’s end or on mine. To combat this I had the server save the states of the words and trie every minute in order to make a fairly good attempt at restoration of the trie in the case of a failure. Lastly, I decided not to save the state of the queue because it might cause issues with how it gets handled on restoration as well as the fact that the queue reads in a separate thread in order to have it running parallel with the addition to the queue so saving the object becomes not so ideal as it is thread locked. 

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- SERVER HOSTING -->
## Server Hosting

The server is currently being hosted as a GCP virtual machine. I have experience with GCP from a lot of my previous projects such as the science fair so it is my default when it comes to cloud computing. In terms of best runtime strategies, I am not exactly super familiar with them so I currently just have my server python script running as a background process.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CLIENT INTERACTION -->
## Client Interaction

Clients interact with the server through the CLI. The CLI can be installed using pip and more instructions on that can be found in the client's <a href="https://github.com/Nathaniel-github/CombinedServerClientRepo/blob/main/TrieCLI/README.md">README</a>. As said previously the communication is done using sockets.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- DOCUMENTATION -->
## Documentation

Documentation can be found in two forms, the first is the <a href="https://github.com/Nathaniel-github/CombinedServerClientRepo/blob/main/TrieCLI/README.md">README.md</a> and the second is documentation on the code which can be found on readthedocs with a direct link to it also located inside the README.md (<a href="https://trieclient.readthedocs.io/en/latest/index.html">or here</a>). There is also documentation on the server which can be found inside the server's <a href="https://github.com/Nathaniel-github/CombinedServerClientRepo/blob/main/TrieServer/README.md">README.md</a> or again through readthedocs (<a href="https://trieserver.readthedocs.io/en/latest/index.html">or here</a>). I should mention that this is my first time creating python docs so they are almost guaranteed to be formatted incorrectly on readthedocs but I hope that it is still easily able to be navigated.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Best README](https://github.com/othneildrew/Best-README-Template)

<p align="right">(<a href="#top">back to top</a>)</p>
