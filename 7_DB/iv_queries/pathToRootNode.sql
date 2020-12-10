DROP PROCEDURE IF EXISTS path_to_root_node;
DELIMITER //
CREATE PROCEDURE path_to_root_node(IN leaf INT )
BEGIN
	DECLARE parent_taxon_id INT;
	DECLARE taxon_name VARCHAR(255);
	DECLARE taxon_rank VARCHAR(255);
	DECLARE path_to_root VARCHAR(255);
	SET @path_to_root = '';
	SELECT taxon_name.name, taxon.node_rank, taxon.parent_taxon_id INTO @taxon_name, @taxon_rank, @parent_taxon_id
	FROM taxon INNER JOIN taxon_name 
	WHERE taxon.taxon_id=taxon_name.taxon_id AND taxon_name.name_class='scientific name' AND taxon.taxon_id=leaf;

	SET @path_to_root=CONCAT(@path_to_root,@taxon_name,':',@taxon_rank);
	
	loop_label: LOOP
	SELECT taxon_name.name, taxon.node_rank, taxon.parent_taxon_id INTO @taxon_name, @taxon_rank, @parent_taxon_id 
	FROM taxon, taxon_name 
	WHERE taxon.taxon_id=taxon_name.taxon_id AND taxon_name.name_class='scientific name' AND taxon.taxon_id=@parent_taxon_id; 
	
	SET @path_to_root=CONCAT(@path_to_root,";",@taxon_name,':',@taxon_rank);
	IF (@parent_taxon_id <> 14610) THEN
	ITERATE loop_label;
	ELSE
	LEAVE loop_label;
	END IF;
	END LOOP;
	SELECT @path_to_root;
END//
DELIMITER ;
