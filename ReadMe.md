## RandomNearing

Definition: _RandomNearing (noun): Neither a portmanteu nor a homonym, yet related to [_Randonneuring_](https://en.wikipedia.org/wiki/Randonneuring), in that it is essentially the opposite: while Randonneuring is organized and far-reaching group bike racing, RandomNearing is random, near and most often performed solo (for good reasons)._ 

Example: _See [RandomNearing.com](https://randomnearing.com)_

### Project Goal
Create a tool that 
* accepts one or more GPX files or Strava activity urls and maps the activities on a scalable map.
* allows for plotting multiple activities on the same map (similar to a heat map but emphasizing overall ground covered more than number of times on each segment)
* Generate a Random score: number of turns per mile?
* Generate a Nearing score: distance biked / circumference of area covered
* Create Colab notebook that allows using the tool in a browser

#### Stretch Goals
Wrap the tool in a website
* Presumably a lambda, or a static website that invokes the tool as a lambda. Possibly a container lambda. TBD.
* Store the activities (or link to activities) _somewhere_


### TODO
- [ ] Pick a Python mapping library
- [ ] Parse GPX file
- [ ] Count number of turns
- [ ] Discover external points, generate circumference s

