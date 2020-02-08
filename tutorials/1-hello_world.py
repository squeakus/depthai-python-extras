import numpy as np # numpy - manipulate the packet data returned by depthai
import cv2 # opencv - display the video stream
import depthai # access the camera and its data packets
import consts.resource_paths # load paths to depthai resources

if not depthai.init_device(consts.resource_paths.device_cmd_fpath):
    print("Error initializing device. Try to reset it.")
    exit(1)

# create the pipeline, establishing the first connection to the device
p = depthai.create_pipeline(config={'streams': ['previewout']})

if p is None:
    print('Error creating pipeline.')
    exit(2)

while True:
    # Retrieve data packets from the device.
    # A data packet contains the video frame data.
    data_packets = p.get_available_data_packets()

    for packet in data_packets:
        print(packet.stream_name)
        elif packet.stream_name == 'previewout':
            data = packet.getData()
            # the format of previewout image is CHW (Channel, Height, Width), but OpenCV needs HWC, so we
            # change shape (3, 300, 300) -> (300, 300, 3)
            data0 = data[0,:,:]
            data1 = data[1,:,:]
            data2 = data[2,:,:]
            frame = cv2.merge([data0, data1, data2])

            cv2.imshow('previewout', frame)

    if cv2.waitKey(1) == ord('q'):
        break

# The pipeline object should be deleted after exiting the loop. Otherwise device will continue working.
# This is required if you are going to add code after exiting the loop.
del p
