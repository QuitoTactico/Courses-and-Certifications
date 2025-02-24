-- List all the taxonomic orders, using their common names, sorted by the number of
-- animals of that order that the zoo has.
--
-- The animals table has (name, species, birthdate) for each individual.
-- The taxonomy table has (name, species, genus, family, t_order) for each species.
-- The ordernames table has (t_order, name) for each order.
--
-- Be careful:  Each of these tables has a column "name", but they don't have the
-- same meaning!  animals.name is an animal's individual name.  taxonomy.name is
-- a species' common name (like 'brown bear').  And ordernames.name is the common
-- name of an order (like 'Carnivores')


-- Mi solución con Joins (no fue la mejor):
SELECT ordernames.name as `taxonomic order`, count(*) as `animals count`
from 
    (animals 
    join taxonomy on animals.species = taxonomy.name) 
    join ordernames on ordernames.t_order = taxonomy.t_order
group by ordernames.t_order
order by `animals count` desc;

-- Sin Joins
select ordernames.name, count(*) as num
    from animals, taxonomy, ordernames
    where animals.species = taxonomy.name
        and taxonomy.t_order = ordernames.t_order
    group by ordernames.name
    order by num desc;

-- Solución con Joins del curso
select ordernames.name, count(*) as num
    from (animals join taxonomy 
            on animals.species = taxonomy.name)
            as ani_tax
        join ordernames
            on ani_tax.t_order = ordernames.t_order
    group by ordernames.name
    order by num desc;

