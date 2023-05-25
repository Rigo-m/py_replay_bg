from init.init_core_variables import init_core_variables

def replay_bg(modality, data, BW, scenario, save_name, 
              sample_time = 5, glucose_model = 'IG', pathology = 't1d', exercise = False, seed = 1,
              bolus_source = 'data', basal_source = 'data', cho_source = 'data', 
              save_suffix = '',
              plot_mode = True, enable_log = True, verbose = True, 
              **kwargs):
    """
    Core function of ReplayBG. Can be used to identify ReplayBG model on the
    given data or to "replay" specific scenarios specified by the given data.

    Parameters
    ----------
    modality : string
        A string that specifies if the function will be used to identify 
        the ReplayBG model on the given data or to replay the scenario specified by 
        the given data. Can be 'identification' or 'replay'
    save_name : string
        A string used to label, thus identify, each output file and result
    save_suffix : string, optional, default: ''
        A string to be attached as suffix to the resulting output files' name
    scenario: string
        A string that specifies whether the given scenario refers to a single-meal scenario or a multi-meal scenario.
        Can be 'single-meal' or 'multi-meal'
    sample_time: int, optional, default: 5
        An integer that specifies the data sample time (in minutes)
    glucose_model: string, optional, default: 'IG'
        A string that specifies the glucose model to use. Can be 'IG' or 'BG'
    pathology: string, optional, default: 't1d' 
        A string that specifies the patient pathology. Can be 't1d', 't2d', 'pbh', 'healthy'
    exercise: boolean, optional, default: False
        A boolean that specifies whether to simulate exercise or not. Can be True or False
    seed: int, optional, default: 1
        An integer that specifies the random seed. For reproducibility
    bolus_source : string, optional, default: `data`
        A string defining whether to use, during replay, the insulin bolus data contained in the `data` timetable (if `data`),
        or the boluses generated by the bolus calculator implemented via the provided `bolusCalculatorHandler` function. 
        Can be `data` or `dss`. It cannot be set if `modality` is `identification`
    basal_source : string, optional, default: `data`
        A string defining whether to use, during replay, the insulin basal data contained in the `data` timetable (if `data`), 
        or the basal generated by the controller implemented via the provided `basalControllerHandler` function (if `dss`), 
        or fixed to the average basal rate used during identification (if `u2ss`). Can be `data`, `u2ss`, or `dss`. It cannot 
        be set if `modality` is `identification`
    cho_source : string, optional, default: `data`
        A string defining whether to use, during replay, the CHO data contained in the `data` timetable (if `data`), 
        or the CHO generated by the meal generator implemented via the provided `mealGeneratorHandler` function. 
        Can be `data` or `generated`. It cannot be set if `modality` is `identification`
    plot_mode : boolean, optional, default: True
        A boolean that specifies whether to show the plot of the results or not. Can be True or False.
    enable_log : boolean, optional, default: True
        A boolean that specifies whether to log the output of ReplayBG not. Can be True or False.
    verbose : boolean, optional, default: True
        A boolean that specifies the verbosity of ReplayBG. Can be True or False.

    Returns
    -------
    None

    Raises
    ------
    None

    See Also
    --------
    None

    Examples
    --------
    None

    References
    --------
    Cappon et al., "ReplayBG: a methodology to identify a personalized model from type 1 diabetes data and simulate glucose concentrations to
    assess alternative therapies", IEEE TBME, 2022 (under revision).

    Copyright
    --------
    (C) 2023 Giacomo Cappon
    This file is part of ReplayBG.
    """
        

    #TODO: add input validators

    # ================ Initialize core variables =========================
    environment, model, sensors, mcmc, dss = init_core_variables(data = data, BW = BW, modality = modality, save_name = save_name, save_suffix = save_suffix, scenario = scenario,
                                                                sample_time = sample_time, glucose_model = glucose_model, pathology = pathology, exercise = exercise, seed = seed,
                                                                bolus_source = bolus_source, basal_source = basal_source, cho_source = cho_source,
                                                                plot_mode = plot_mode, enable_log = enable_log, verbose = verbose)
    # ====================================================================

    print(model)