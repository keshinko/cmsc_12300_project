from group_objects import MrBoxAstroObjects


# Test code:
if __name__ == "__main__":
    # initialize MRJob:
    csv_input = '5218597(50).csv'
    mr_job = MrBoxAstroObjects(args=['-r', 'local', csv_input])
    with mr_job.make_runner() as runner:
        runner.run()
        # For every output tuple from the MRJob:
        for line in runner.stream_output():
            # list_of_astroobjs here will contain items within a single box:
            bounds, list_of_astroobjs = mr_job.parse_output_line(line)
            print(bounds, list_of_astroobjs)
            #Some lists will be empty (when only one or zero objects in a box):
            if list_of_astroobjs:
                for astro_obj in list_of_astroobjs:
                    if astro_obj:
                        # This just prints number of visits of this astro object:
                        print(astro_obj.rand_walk_visits)