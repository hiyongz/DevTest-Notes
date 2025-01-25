def angleSetX(angle):
    """设置X轴角度
    
    :param angle: 角度值
    :return : 无
    """
    # curPos = self.getCurrentPositionX()
    curPos = '-30.0000'
    curPos = float(curPos)
    print(curPos)

    if angle%30 != 0:
        print("error")

    diffangle = curPos - angle
    step = int(abs(diffangle)/30)
    print(step)
    # if diffangle < 0:



angleSetX(20)