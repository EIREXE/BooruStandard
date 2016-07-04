# The two systems
Boorus traditionally used underscore based systems:
> red_hair blue_eyes order:score score:>10

However, this system is primitive and counter intuitive, a comma based system can be implemented and do more things in a more intuitive way:

> red hair or blue hair or green hair, blue eyes, order by score, score > 10

This will find all images that contain a character that has green, blue or red hair and blue eyes and it will sort the images by score but will only contain images that have a score of over 10 points.

# Tag categories
Tags should have categories that are assignated mainly for presentation purposes and serve no use when searching, for example, wether a tag represents either a character("Mario"), a series("Super Mario Bros."), an artist ("unya") or a normal tag("Red Hair"):

![](https://i.imgur.com/inmnMk6.png)

This allows you to present stuff in a better way, instead of presenting the characters tags artist tags and series tags in the same place.

# Ways of doing tagging

Traditionally Boorus have had to ways of dealing with tagging and what should be a tag, there are some boorus (Specially those centered around R34) that prefer to simply list who the characters are, their series and them some minimal description, for example what software it was animated in (Source Filmmaker) or wether or not the image is animated.

That is one way of doing it, however what most boorus opt for is a more detailed way of tagging in the section on top of this one you can find a perfect example from danbooru.

## Comma-based system

### Description
Comma-based systems uses commas (,) to separate tags.

It is more intuitive for the user as it is more similar to a written list, and it allows much more english-like word formations, that's why it's the one chosen to become the standard way of doing tag searches.

Tags are not case sensitive.

Example:
>red hair or green hair, blue eyes, sort by score, score > 10

### Ordering
Ordering has a special case for comments, where referring to comments actually means referring to the comment count.
#### Order by
>Order by score

>Order by descending comments

>Order by ascending comments


#### Comparative
Examples:
> Score > 10

> Comments < 10

> Score => 10

> Score is 10

# Reserved characters
The reserved characters that are not allowed in tags are the following:

**,**

### Example implementation
All tags should be saved as an individual list, it is not necessary to store the raw format of the tags ("red hair, blue hair"), instead storing them as individual objects that have a two-way relationship with the image should be done, so that the image object itself contains all the tags it uses and the tag object contains all the images that have that tag, plus other information like tag categories, this is also for efficiency reasons, querying a tag and seeing what images it contains is faster than seeing what images contain certain tag, as you are not querying all the images at the same time.

A classical implementation of tags goes as follows:
* Get the user input, in this case "red hair or green hair, blue eyes, sort by score, score > 10"
* Each part is called a term, to get all terms you split the string by the comma, resulting in an array or similar, depending on your language:

>["red hair or green hair", " blue eyes", " order by score", " score > 10"]

* Trimming is then done to remove the trailing and starting spaces on all terms:
>["red hair or green hair", "blue eyes", "order by score", "score > 10"]

* Now it's time to parse the terms, iterating through them, an example implementation of this can be found on [parsing_example.py](parsing_example.py)
