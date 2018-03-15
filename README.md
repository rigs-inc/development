# E-commerce API

## Requirements

The user must be able to

- Create a new product.
- Read|Get a product by ID.
- Update the product's price.
- Delete a product by ID.
- Get a complete list of products.
    + Should be sortable by name (default), and by popularity (likes). 
    + Should have pagination functionality.
    + Search through the products by name.
- Like a product
- Buy a product.
    + Buying a product should reduce its stock.
- Keep a log of all the purchases (who bought it, how many, when).

**Product Data Structure**:

```
{
    id: int,
    name: string,
    npc: string,
    stock: int,
    price: int,
    likes: int,
    last_update: date
}
```

## Security requirements

### Login

**Admin Users**

- Can Add|Delete products. 
- Can modify price of the products.

**Registered Users**

- Can buy a product.
- Can like a product.

**Everyone**
- Can get a list of all the products.
- Can use the search feature.

## Testing requiremnets

- Publish your work using Heroku and sharing the link with us.

## Keep in mind

- You are free to use any package, framework, library and weapons for the battle as long as you can justify their use.
- You may use any kind of database you like.
- Provide a database dump so we can replicate the database locally.
- Follow best RESTful services practices.
- Use git and do small commits to facilitate the evaluation of progress.
- Include a *readme.m* file with instructions on how to **USE** & **Setup** your project locally to test it. (This is super important, if we cannot install it and run it easily we cannot evaluate it).
- Upload your solution to your GitHub account and share a link with your evaluator.
- The test has been designed with enough time to do a good job, so don’t cut any corners, take your time and watch for quality.

## Time to complete: 7 days

Looking forward to see your code

Good luck!
We hope to hear from you soon, have fun! 