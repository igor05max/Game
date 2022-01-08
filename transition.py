from field import field_, dist


def transition(x_player, y_player):
    for i in field_:
        if field_[i] == "2":
            if dist(x_player, y_player, i[0], i[1]) < 80:
                return True
            return False
