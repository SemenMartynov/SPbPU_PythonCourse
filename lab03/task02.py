# TODO Напишите функцию find_common_participants
def find_common_participants(first_group_list, second_group_list, separator=','):
    """
    Определение, кто является общими участниками для обеих групп
    """
    first_group = set(first_group_list.split(separator))
    second_group = set(second_group_list.split(separator))

    groups_intersection = list(first_group.intersection(second_group))
    groups_intersection.sort()

    return groups_intersection


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
common_participants = find_common_participants(
    participants_first_group, participants_second_group, "|")
print(common_participants)
