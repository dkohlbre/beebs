#!/bin/bash

# Output logs
source $TEST_CONFIG
#Can't set -e here, some tests 'fail' (see crc32's strange compare)
#set -e

for tst in bin/*; do
    tst=$(basename $tst)

    echo "Running $tst"
    for RUN_N in $(seq $REPS); do

        BASE_LOG_FILE=${TEST_LOG_DIR}/base_${tst}_${RUN_N}.log
        KEYSTONE_LOG_FILE=${TEST_LOG_DIR}/keystone_${tst}_${RUN_N}.log

        if [[ $RUN_BASELINE == 1 ]]; then
            ./bin/${tst} > ${BASE_LOG_FILE} 2> ${BASE_LOG_FILE}.err
        fi
        if [[ $RUN_KEYSTONE == 1 ]]; then
            ${TEST_RUNNER} ./bin/${tst} ${EYRIE_FULL_SUPPORT} ${DEFAULT_USZ} ${DEFAULT_FSZ} 0 0 > ${KEYSTONE_LOG_FILE} 2> ${KEYSTONE_LOG_FILE}.err
        fi
    done
done
