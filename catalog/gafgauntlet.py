

def get_gauntlet_scores(gauntlet_dict):

      #define dict details
      holes = gauntlet_dict["holes"]
      slot_model = gauntlet_dict["slot_model"]
      stableford_model = gauntlet_dict["stableford_model"]

      #define players by slot
      slot_names = slot_model.objects.all()
      slot_list = []
      for gauntlet_name in slot_names:
        if gauntlet_name.player_name == None:
            slot_list.append(None)
        else:
            # slot_list.append(name.player_name)
            slot_list.append(gauntlet_name.player_name.name)

      #define scores in gauntlet holes
      fields = stableford_model._meta.get_fields()

      full_list = []

      for hole in holes:
          inner_list = []
          try:
              target_hole=stableford_model.objects.get(hole=hole)

              for field in fields:
                  if field.name == 'id' or field.name == 'hole':
                      pass
                  else:
                      field_value = getattr(target_hole, field.name)
                      inner_list.append(field_value)
              full_list.append(inner_list)

              #combine lists together
              combined_list = []
              for counter, field in enumerate(fields):
                  individual_list = []
                  if field.name == 'id' or field.name == 'hole':
                      pass
                  else:
                      adj_counter = counter - 2
                      individual_list.append(slot_list[adj_counter])
                      sum_list = []
                      for list_counter, value in enumerate(full_list):
                          sum_list.append(full_list[list_counter][adj_counter])
                          summed_list = sum(sum_list)
                      individual_list.append(summed_list)
                      combined_list.append(individual_list)
          except:
              combined_list = None

      print(f'Gauntlet Scores: {combined_list}')
      return combined_list
