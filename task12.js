public_users.get("/author/:author", async (req, res) => {
  // get array of matching book objects
  const matchingBooks = Object.values(await books).filter(
    (book) => book.author.toLowerCase() === req.params.author.toLowerCase()
  );
  if (matchingBooks.length > 0) {
    return res.status(200).send(JSON.stringify(matchingBooks, null, 4));
  } else {
    return res.status(404).json({ message: "No books by that author." });
  }
});
