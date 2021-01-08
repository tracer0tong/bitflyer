from nose.tools import *

from bitflyer.public import Public


def test_getticker():
    m1 = Public()
    ok_(isinstance(m1.getticker().get('product_code'), str))
    ok_(isinstance(m1.getticker().get('volume_by_product'), float))
    ok_(isinstance(m1.getticker().get('total_bid_depth'), float))
    ok_(isinstance(m1.getticker().get('best_ask'), float))
    ok_(isinstance(m1.getticker().get('timestamp'), str))
    ok_(isinstance(m1.getticker().get('product_code'), str))
    ok_(isinstance(m1.getticker().get('total_ask_depth'), float))
    ok_(isinstance(m1.getticker().get('ltp'), float))
    ok_(isinstance(m1.getticker().get('tick_id'), int))
    ok_(isinstance(m1.getticker().get('best_ask_size'), float))
    ok_(isinstance(m1.getticker().get('volume'), float))
    ok_(isinstance(m1.getticker().get('best_bid_size'), float))
    ok_(isinstance(m1.getticker().get('best_bid'), float))


def test_getexecutions():
    m1 = Public()
    ok_(isinstance(m1.getexecutions(), list))
    ok_(isinstance(m1.getexecutions()[0].get('price'), float))
    ok_(isinstance(m1.getexecutions()[0].get('exec_date'), str))
    ok_(isinstance(m1.getexecutions()[0].get('size'), float))
    ok_(isinstance(m1.getexecutions()[0].get('side'), str))
    ok_(isinstance(m1.getexecutions()[0].get('sell_child_order_acceptance_id'), str))
    ok_(isinstance(m1.getexecutions()[0].get('id'), int))
    ok_(isinstance(m1.getexecutions()[0].get('buy_child_order_acceptance_id'), str))


def test_getboard():
    m1 = Public()
    ok_(isinstance(m1.getboard(), dict))
    ok_(isinstance(m1.getboard().get('mid_price'), float))
    ok_(isinstance(m1.getboard().get('bids')[0].get('size'), float))
    ok_(isinstance(m1.getboard().get('bids')[0].get('price'), float))
    ok_(isinstance(m1.getboard().get('asks')[0].get('size'), float))
    ok_(isinstance(m1.getboard().get('asks')[0].get('price'), float))


def test_gethealth():
    m1 = Public()
    ok_(isinstance(m1.gethealth(), dict))
    ok_(isinstance(m1.gethealth().get('status'), str))
