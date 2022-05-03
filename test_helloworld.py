from helloworld import main


def test_main(capsys):
    main()
    captured = capsys.readouterr()
    assert "hello world" in captured.out
