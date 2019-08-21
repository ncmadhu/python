def find_overlap(x1, point1, x2, point2):
    x3 = max(x1, x2)
    point3 = min(x1 + point1, x2 + point2)

    if x3 >= point3:
        return(None, None)

    point3 = point3 - x3
    return (x3,point3)

def overlap_rectangle(rect1, rect2):
    x_overlap, width = find_overlap(rect1['left_x'], rect1['width'],
                          rect2['left_x'], rect2['width'])
    y_overlap, height = find_overlap(rect1['bottom_y'], rect1['height'],
                          rect2['bottom_y'], rect2['height'])
    if not width or not height:
     return {"left_x": None,
             "bottom_y": None,
             "width": None,
             "height": None}
    return {"left_x": x_overlap,
             "bottom_y": y_overlap,
             "width": width,
             "height": height}

if __name__ == "__main__":
    print(overlap_rectangle({"left_x": 3,
             "bottom_y": 2,
             "width": 10,
             "height": 10}, {"left_x": 7,
             "bottom_y": 7,
             "width": 7,
             "height": 6}))