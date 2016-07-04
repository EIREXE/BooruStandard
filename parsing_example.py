#This code is untested and probably won't work, it does not even have a single import, i use SQLAlchemy styled querying here, but Maria or Mongo should be able to do this, in fact I think they might be able to do it more efficiently, but don't you dare quote me on that.

def search_query(query):
    terms = query.strip().lower().split(',')
    for term in terms:
        filters = list()
        # Trim the sides of the search query
        term = term.strip()
        # Or
        if term.contains(' or '):
            or_filter = list()
            # Split the or query by the or substring
            or_terms = term.split(' or ')
            for or_term in or_terms:
                or_term = term.strip()
                tags_to_or = list()
                # Find the tag in the database by it's name, the ilike here denotes case insensitvity
                or_tag = Tags.query.filter(Tag.name.ilike(or_term)).first()
                # If the tag exists add it to the filter
                if or_tag:
                    or_filter.append(or_tag)
                    # Make all tag filters into an or filter and add it to the global filter
                    filters.append(_or(*or_filter))
                    continue
                    # Order by score
                    order_by_score = False
        if term == "order by score":
            order_by_score = True
            query = Image.query.filter(filters)
    if order_by_score:
        query.order_by(Image.score)
    return query.all()
