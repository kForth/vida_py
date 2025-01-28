def test_MessageTiming():
    """Test the MessageTiming class"""
    from vida_py.timing import MessageTiming, Session

    with Session() as session:
        result = (
            session.query(MessageTiming).filter(MessageTiming.MessageTimingId == 0).one()
        )
        assert result is not None and result.P1max == 40


def test_Requests():
    """Test the Requests class"""
    from vida_py.timing import Requests, Session

    with Session() as session:
        result = session.query(Requests).filter(Requests.ECU_variant == 340).one()
        assert result is not None and result.B1 == 171


def test_TimeoutAndResend():
    """Test the TimeoutAndResend class"""
    from vida_py.timing import Session, TimeoutAndResend

    with Session() as session:
        result = (
            session.query(TimeoutAndResend)
            .filter(TimeoutAndResend.TimeoutAndResendId == 0)
            .one()
        )
        assert result is not None and result.Timeout == 3000
