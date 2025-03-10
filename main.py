import math

# =============================================================================
# 1) EXISTING PLANTS
# =============================================================================
existing_plants = [
    {
        'name': 'd1',
        'type': 'nuclear',
        'capacity_mw': 800.0,
        'reliability_pct': 93.7,
        'efficiency': 0.3353,  # 33.53%
        'loan_payment_my_per_year': 308.1,  # M€/year
        'remaining_payments_yrs': 19,
        'fixed_om_my_per_year': 91.8,
        'status': 'available',
        'first_round_active': -9,
        'priority': 1,
        'fuel_cost_me_per_mwh_th': 0.0,
        'variable_om_me_per_mwh': 0.0,
        # New parameter: how many MW we want to bid this round
        'bid_mw': 800.0
    },
    {
        'name': 'd2',
        'type': 'powderCoal',
        'capacity_mw': 600.0,
        'reliability_pct': 94.5,
        'efficiency': 0.3901,
        'loan_payment_my_per_year': 59.6,
        'remaining_payments_yrs': 19,
        'fixed_om_my_per_year': 74.3,
        'status': 'available',
        'first_round_active': -6,
        'priority': 2,
        'fuel_cost_me_per_mwh_th': 0.0,
        'variable_om_me_per_mwh': 0.0,
        'bid_mw': 600.0
    },
    {
        'name': 'd3',
        'type': 'powderCoal',
        'capacity_mw': 600.0,
        'reliability_pct': 91.6,
        'efficiency': 0.3748,
        'loan_payment_my_per_year': 64.6,
        'remaining_payments_yrs': 19,
        'fixed_om_my_per_year': 19.0,
        'status': 'available',
        'first_round_active': -4,
        'priority': None,
        'fuel_cost_me_per_mwh_th': 0.0,
        'variable_om_me_per_mwh': 0.0,
        'bid_mw': 600.0
    },
    {
        'name': 'd4',
        'type': 'wind',
        'capacity_mw': 50.0,
        'reliability_pct': 95.2,
        'efficiency': 0.0,  # wind not typically expressed as efficiency
        'loan_payment_my_per_year': 10.9,
        'remaining_payments_yrs': 14,
        'fixed_om_my_per_year': 2.4,
        'status': 'available',
        'first_round_active': -3,
        'priority': 3,
        'fuel_cost_me_per_mwh_th': 0.0,
        'variable_om_me_per_mwh': 0.0,
        'bid_mw': 50.0
    },
    {
        'name': 'd5',
        'type': 'wind',
        'capacity_mw': 50.0,
        'reliability_pct': 95.8,
        'efficiency': 0.0,
        'loan_payment_my_per_year': 9.9,
        'remaining_payments_yrs': 14,
        'fixed_om_my_per_year': 2.4,
        'status': 'available',
        'first_round_active': 0,
        'priority': 4,
        'fuel_cost_me_per_mwh_th': 0.0,
        'variable_om_me_per_mwh': 0.0,
        'bid_mw': 50.0
    },
    {
        'name': 'd6',
        'type': 'naturalgasCCGT',
        'capacity_mw': 500.0,
        'reliability_pct': 92.9,
        'efficiency': 0.5188,
        'loan_payment_my_per_year': 33.7,
        'remaining_payments_yrs': 14,
        'fixed_om_my_per_year': 77.0,
        'status': 'available',
        'first_round_active': -14,
        'priority': 7,
        'fuel_cost_me_per_mwh_th': 0.0,
        'variable_om_me_per_mwh': 0.0,
        'bid_mw': 500.0
    },
    {
        'name': 'd7',
        'type': 'naturalgasOCGT',
        'capacity_mw': 50.0,
        'reliability_pct': 93.9,
        'efficiency': 0.3674,
        'loan_payment_my_per_year': 3.3,
        'remaining_payments_yrs': 9,
        'fixed_om_my_per_year': 1.3,
        'status': 'available',
        'first_round_active': -8,
        'priority': 5,
        'fuel_cost_me_per_mwh_th': 0.0,
        'variable_om_me_per_mwh': 0.0,
        'bid_mw': 50.0
    },
    {
        'name': 'd8',
        'type': 'naturalgasOCGT',
        'capacity_mw': 50.0,
        'reliability_pct': 94.8,
        'efficiency': 0.3740,
        'loan_payment_my_per_year': 3.2,
        'remaining_payments_yrs': 9,
        'fixed_om_my_per_year': 33.3,
        'status': 'available',
        'first_round_active': -5,
        'priority': 9,
        'fuel_cost_me_per_mwh_th': 0.0,
        'variable_om_me_per_mwh': 0.0,
        'bid_mw': 50.0
    },
    {
        'name': 'd9',
        'type': 'solar',
        'capacity_mw': 20.0,
        'reliability_pct': 94.8,
        'efficiency': 0.0,
        'loan_payment_my_per_year': 1.3,
        'remaining_payments_yrs': 14,
        'fixed_om_my_per_year': 0.4,
        'status': 'available',
        'first_round_active': -1,
        'priority': 6,
        'fuel_cost_me_per_mwh_th': 0.0,
        'variable_om_me_per_mwh': 0.0,
        'bid_mw': 20.0
    },
    {
        'name': 'd10',
        'type': 'biomass',
        'capacity_mw': 100.0,
        'reliability_pct': 95.2,
        'efficiency': 0.3959,
        'loan_payment_my_per_year': 10.3,
        'remaining_payments_yrs': 19,
        'fixed_om_my_per_year': 13.2,
        'status': 'available',
        'first_round_active': -3,
        'priority': 10,
        'fuel_cost_me_per_mwh_th': 0.0,
        'variable_om_me_per_mwh': 0.0,
        'bid_mw': 100.0
    }
]

# =============================================================================
# 2) NEW INVESTMENT OPTIONS (plants you can build)
# =============================================================================
investment_options = [
    {
        'type': 'biomass',
        'reliability_pct': 96.0,
        'efficiency': 0.412,
        'construction_time_yrs': 4,
        'permit_time_yrs': 1,
        'life_expectancy_yrs': 40,
        'down_payment_me_per_mw': 0.297,
        'loan_payment_me_per_mw_per_year': 0.095,
        'num_loan_payments': 20,
        'om_cost_me_per_mw_per_year': 0.130,
        'capacity_min_mw': 400,
        'capacity_max_mw': 1000,
        "bid_mw": 20
    },
    {
        'type': 'powderCoal',
        'reliability_pct': 96.0,
        'efficiency': 0.412,
        'construction_time_yrs': 4,
        'permit_time_yrs': 1,
        'life_expectancy_yrs': 40,
        'down_payment_me_per_mw': 0.277,
        'loan_payment_me_per_mw_per_year': 0.089,
        'num_loan_payments': 20,
        'om_cost_me_per_mw_per_year': 0.121,
        'capacity_min_mw': 400,
        'capacity_max_mw': 1000,
        "bid_mw": 20
    },
    {
        'type': 'solar',
        'reliability_pct': 96.0,
        'efficiency': 0.0,
        'construction_time_yrs': 1,
        'permit_time_yrs': 1,
        'life_expectancy_yrs': 25,
        'down_payment_me_per_mw': 0.155,
        'loan_payment_me_per_mw_per_year': 0.060,
        'num_loan_payments': 15,
        'om_cost_me_per_mw_per_year': 0.020,
        'capacity_min_mw': 100,
        'capacity_max_mw': 700,
        "bid_mw": 20
    },
    {
        'type': 'naturalgasOCGT',
        'reliability_pct': 96.0,
        'efficiency': 0.392,
        'construction_time_yrs': 2,
        'permit_time_yrs': 0,
        'life_expectancy_yrs': 30,
        'down_payment_me_per_mw': 0.115,
        'loan_payment_me_per_mw_per_year': 0.059,
        'num_loan_payments': 10,
        'om_cost_me_per_mw_per_year': 0.025,
        'capacity_min_mw': 100,
        'capacity_max_mw': 500,
        "bid_mw": 20
    },
    {
        'type': 'naturalgasCCGT',
        'reliability_pct': 96.0,
        'efficiency': 0.585,
        'construction_time_yrs': 3,
        'permit_time_yrs': 1,
        'life_expectancy_yrs': 30,
        'down_payment_me_per_mw': 0.150,
        'loan_payment_me_per_mw_per_year': 0.058,
        'num_loan_payments': 15,
        'om_cost_me_per_mw_per_year': 0.063,
        'capacity_min_mw': 500,
        'capacity_max_mw': 900,
        "bid_mw": 20
    },
    {
        'type': 'nuclear',
        'reliability_pct': 96.0,
        'efficiency': 0.34,
        'construction_time_yrs': 5,
        'permit_time_yrs': 2,
        'life_expectancy_yrs': 50,
        'down_payment_me_per_mw': 1.200,
        'loan_payment_me_per_mw_per_year': 0.385,
        'num_loan_payments': 20,
        'om_cost_me_per_mw_per_year': 0.111,
        'capacity_min_mw': 900,
        'capacity_max_mw': 1300,
        "bid_mw": 20
    },
    {
        'type': 'wind',
        'reliability_pct': 96.0,
        'efficiency': 0.0,
        'construction_time_yrs': 1,
        'permit_time_yrs': 1,
        'life_expectancy_yrs': 25,
        'down_payment_me_per_mw': 0.485,
        'loan_payment_me_per_mw_per_year': 0.187,
        'num_loan_payments': 15,
        'om_cost_me_per_mw_per_year': 0.047,
        'capacity_min_mw': 100,
        'capacity_max_mw': 700,
        "bid_mw": 20
    }
]

def calculate_marginal_cost(plant, include_capital_in_bid=False):
    """
    Calculates a 'marginal cost' or 'bid price' for an *existing* plant dictionary,
    based on:
      - Fuel cost / efficiency
      - Variable O&M
      - (Optionally) a share of capital/loan + fixed O&M spread over expected generation.
    """
    eff = plant.get('efficiency', 1.0)
    if eff <= 0:
        eff = 1.0

    # 1) Fuel cost (assuming 'fuel_cost_me_per_mwh_th' is per MWh(th))
    fuel_cost = plant.get('fuel_cost_me_per_mwh_th', 0.0) / eff
    
    # 2) Variable O&M
    var_om = plant.get('variable_om_me_per_mwh', 0.0)
    
    # 3) Capital / fixed cost portion (if included)
    capital_component = 0.0
    if include_capital_in_bid:
        capacity = plant.get('capacity_mw', 0.0)
        annual_hours = 8760
        # For net electric capacity, if capacity_mw is already "electric MW," just use it;
        # if it's "thermal MW," multiply by efficiency. Adjust as per your data definitions:
        capacity_e = bid_mw * eff  # optional if capacity is thermal; remove if it's net.
        
        # Annual MWh(e)
        expected_annual_mwh = capacity_e * annual_hours
        
        loan = plant.get('loan_payment_my_per_year', 0.0)
        fixed_om = plant.get('fixed_om_my_per_year', 0.0)
        
        if expected_annual_mwh > 0:
            capital_component = (loan + fixed_om) / expected_annual_mwh
    
    mc = fuel_cost + var_om + capital_component
    return mc

def main():
    # Example usage: compute marginal costs for each plant, with/without capital
    print("Marginal Costs for each *existing* Plant (excluding capital costs):")
    for p in existing_plants:
        mc_no_cap = calculate_marginal_cost(p, include_capital_in_bid=False)
        print(f"  {p['name']:>3} ({p['type']}) -> MC: {mc_no_cap:.4f} M€/MWh, Bid MW: {p['bid_mw']:.1f}")
    
    print("\nMarginal Costs for each *existing* Plant (including capital + fixed O&M):")
    for p in existing_plants:
        mc_with_cap = calculate_marginal_cost(p, include_capital_in_bid=True)
        print(f"  {p['name']:>3} ({p['type']}) -> MC: {mc_with_cap:.4f} M€/MWh, Bid MW: {p['bid_mw']:.1f}")
    
    # Example: building a new wind plant from investment options
    print("\nExample of new investment (wind):")
    new_wind = investment_options[-1]  # the last in the list is wind
    chosen_capacity = 400.0  # example choice
    total_down_payment = new_wind['down_payment_me_per_mw'] * chosen_capacity
    annual_loan_payment = new_wind['loan_payment_me_per_mw_per_year'] * chosen_capacity
    print(f"  Building {chosen_capacity:.1f} MW of {new_wind['type']}")
    print(f"    Down payment = {total_down_payment:.3f} M€ (one-time)")
    print(f"    Annual loan  = {annual_loan_payment:.3f} M€/year")

if __name__ == "__main__":
    main()
