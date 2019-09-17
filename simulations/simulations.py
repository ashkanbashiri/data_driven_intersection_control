from vissim_utils.sim import generate_phase_times, run_simulation, printProgressBar
import sys
import time
import datetime
import multiprocessing
import win32com.client as com
import os


def main():
    global start_time
    start_time = time.time()
    fair_scheme = 'fair'
    relative_scheme = 'relative'
    schemes = [fair_scheme,relative_scheme]
    n_phase = 4
    c_times = list(xrange(50,155,5))#CYCLE TIMES = [50,55,...,150] seconds
    sum_flows = list(xrange(35,101,5)) # TOTAL_FLOWS = [35,...,50,51,....,99,100]% of Saturation Flow Rate
    sum_flows = [float(x)/100 for x in sum_flows]
    lost_times = list(xrange(4,32,4)) # LOST_TIMES = [4,8,12,16,20] seconds
    flow_ratios = [ [0.25, .25, .25, .25], [0.1, 0.4, 0.1, 0.4], [0.2, 0.3, 0.2, 0.3], [0.1, 0.1, 0.4, 0.4],
                   [0.1, .1, .1, .7], [0.2, 0.2, 0.5, 0.1]]
    first_time = 1
    num_simulations = len(sum_flows)*len(lost_times)*len(c_times)*len(flow_ratios)*2
    print "Starting to run %d simulations" %(num_simulations)
    sim_number = 0
    last_checkpoint = 1692+489+187+432+1436+324+2657+219+2334+555+1499+637+416+62+336+111+\
                      99+131+1457+508+183+603+583+1479+503+1890+407+90+1329
    global Vissim
    close_vis = False
    restart_vissim = False
    for sum_flow in sum_flows:
        for lost_time in lost_times:
            for ct in c_times:
                for i in xrange(len(flow_ratios)):
                    ratios = [x * sum_flow for x in flow_ratios[i][:]]
                    for scheme_number in xrange(2):
                        _progress(sim_number, num_simulations)
                        phase_times = generate_phase_times(ct,sum_flow,flow_ratios[i][:],lost_time,n_phase,scheme=schemes[scheme_number])
                        if sim_number>last_checkpoint:
                            if close_vis is True:
                                restart_vissim = True
                            else:
                                restart_vissim = False
                            if sim_number%100 == 0:
                                close_vis = True
                            else:
                                close_vis = False
                            run_simulation(ct,phase_times,lost_time,ratios,first_time, 'results_sep08_30.csv',
                                           close_vissim=close_vis, reset_vissim=restart_vissim)
                            first_time = 0
                        sim_number +=1


    sys.stdout.write('\rAll simulations Completed Sucessfully!')


def _progress(count, total_size):
    global start_time
    elapsed_time = int(time.time() - start_time)
    sys.stdout.write('\r%.2f%% Completed, ' % (float(count) / float(total_size) * 100.0) +
                     '\tElapsed Time: {}'.format(str(datetime.timedelta(seconds=elapsed_time))))
    sys.stdout.flush()


if __name__ == "__main__":
    main()


'''
                            while not done:
                                p = multiprocessing.Process(target=run_simulation, args=(ct,phase_times,
                                                                                           lost_time,ratios,first_time,
                                                                                           'results_sep08_2.csv'))
                                p.start()
                                p.join(60)
                                if p.is_alive():
                                    print "Vissim is Not Responding..."
                                    print "Terminating run #{}".format(sim_number)
                                    p.terminate()
                                    continue
                                #p.join()
                                else:
                                    first_time=0
                                    done = True
'''