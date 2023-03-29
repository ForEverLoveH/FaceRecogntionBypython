import os
import sys

import get_faces_from_camera_tkinter as get
import face_reco_from_camera_ot as face
import face_reco_from_camera_single_face as single
import features_extraction_to_csv as features


def main():
    if 'PyPy' in sys.version:
        print('PyPy')
    if os.name == 'java':
        print('Jython')
    if sys.version.startswith('IronPython'):
        print('IronPython')
    print('CPython')

    index = input("(0)人脸数据导入\n(1)人脸识别\n(2)人脸识别-中文名称\n(3)训练人脸数据集\n(-1)退出\n")
    if index == "0":
        get.main()
        main()
    if index == "1":
        face.main()
        main()
    if index == "2":
        single.main()
        main()
    if index == "3":
        features.main()
        main()
    if index != "0" and index != "1" and index != "2":
        return 0


if __name__ == '__main__':
    main()

